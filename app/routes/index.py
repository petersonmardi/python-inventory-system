from flask import (
    Blueprint, 
    render_template, 
    url_for
    )

from ..models.inventory_model import InventoryModel

from ..extensions import db

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    columns = InventoryModel.query.all()
    return render_template('index.html', columns=columns)