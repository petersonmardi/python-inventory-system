from flask import (
    Blueprint, 
    render_template, 
    request, 
    jsonify, 
    url_for, 
    redirect
    )

from ..models.inventory_model import InventoryModel

from ..extensions import db

update_item_bp = Blueprint('update_item', __name__)

@update_item_bp.route('/update/<int:id>/')
def update(id):

    product = InventoryModel.query.filter_by(id=id).one()

    return render_template('update_item.html', product=product)

@update_item_bp.route('/update_item/<int:id>/', methods=['POST', 'GET'])
def update_item(id):
    # Get data

    product = InventoryModel.query.filter_by(id=id).one()

    if request.method == 'POST':

        error = None

        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        column_of_data = [name, description, price, quantity]

        for element in column_of_data:
            if element is None:
                error = 'Input cannot be empty'
                if error is not None:
                    flash(error)
            else:
                product.name = name
                product.description = description
                product.price = price
                product.quantity = quantity

                db.session.commit()

                return redirect(url_for('index.index'))