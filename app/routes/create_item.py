from flask import (
    Blueprint, 
    render_template, 
    request, 
    flash, 
    url_for, 
    redirect
    )

from ..models.inventory_model import InventoryModel

from ..extensions import db

from ..extensions import login_required

create_bp = Blueprint('create_item', __name__)

@create_bp.route('/create')
@login_required
def create():
    return render_template('create_item.html')

@create_bp.route('/create_item', methods=['POST', 'GET'])
@login_required
def create_item():

    if request.method == 'POST':

        error = None

        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        if not name:
            error = 'Name cannot be empty'
        elif not description:
            error = 'Description cannot be empty'
        elif not price:
            error = 'Price cannot be empty'
        elif not quantity:
            error = 'Quantity cannot be empty'

        if error is None:
            _columns = InventoryModel(
                        name=name,
                        description=description,
                        price=price,
                        quantity=quantity
                        )
            db.session.add(_columns)
            db.session.commit()

            return redirect(url_for('index.index'))

        flash(error)

    return render_template('create_item.html')
