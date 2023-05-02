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

delete_bp = Blueprint('delete_item', __name__)

@delete_bp.route('/delete_item/<int:id>/')
def delete_item(id):
    _item_ = InventoryModel.query.filter_by(id=id).one()

    db.session.delete(_item_)
    db.session.commit()
    return redirect(url_for('index.index'))

    # Get form data
    # item_id = int(request.form['id'])
    # Delete from database
    # conn = sqlite3.connect('inventory.db')
    # c = conn.cursor()
    # c.execute("DELETE FROM items WHERE id=?", (item_id,))
    # conn.commit()
    # conn.close()

    # return jsonify({'success': True})