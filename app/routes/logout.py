from flask import (
    Blueprint,
    request,
    url_for, 
    redirect
    )

from ..extensions import login_required, logout_user

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))