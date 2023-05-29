from flask import (
    Blueprint, 
    render_template, 
    request,
    flash,
    url_for, 
    redirect
    )

from ..extensions import db

from ..models.user_management import User

from werkzeug.security import check_password_hash

from ..extensions import login_required, login_user


login_bp = Blueprint('login', __name__)

@login_bp.route('/login')
def login():
    return render_template('auth/login.html')


@login_bp.route('/login/user', methods=['POST', 'GET'])
def login_existing_user():

    if request.method == 'POST':
        error = None
        email = request.form['email']
        password = request.form['password']

        user_ = User.query.filter_by(email=email).first()

        if user_ is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user_.password, password):
            error = 'Incorrect password.'
        

        if error is None:
            login_user(user_)
            return redirect(url_for('index.index'))
    
        flash(error)
    
    return render_template('auth/login.html')
