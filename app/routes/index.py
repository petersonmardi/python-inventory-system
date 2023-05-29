from flask import (
    Blueprint, 
    render_template, 
    url_for
    )

from ..models.inventory_model import InventoryModel

from ..extensions import db
from ..extensions import login_required

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
@login_required
def index():
    columns = InventoryModel.query.all()
    return render_template('index.html', columns=columns)