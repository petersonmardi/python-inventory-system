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

create_bp = Blueprint('create_item', __name__)

@create_bp.route('/create')
def create():
    return render_template('create_item.html')

@create_bp.route('/create_item', methods=['POST', 'GET'])
def create_item():
    # Get form data

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
                _columns = InventoryModel(
                                    name=name,
                                    description=description,
                                    price=price,
                                    quantity=quantity
                )
                db.session.add(_columns)
                db.session.commit()

                return redirect(url_for('index.index'))
                # return jsonify({'success': True})

    # Insert into database
    # conn = sqlite3.connect('inventory.db')
    # c = conn.cursor()
    # c.execute("INSERT INTO items (name, description, price, quantity) VALUES (?, ?, ?, ?)",
    #           (name, description, price, quantity))
    # conn.commit()
    # conn.close()
