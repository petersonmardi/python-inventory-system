from flask import (
    Blueprint, 
    render_template, 
    request,
    url_for, 
    redirect,
    flash
    )
from ..extensions import db

from ..models.user_management import User

from werkzeug.security import generate_password_hash

register_bp = Blueprint('register', __name__)

@register_bp.route('/register')
def register():
    return render_template('auth/register.html')

@register_bp.route('/register/new_user', methods=['POST', 'GET'])
def register_new_user():

    if request.method == 'POST':

        error = None

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        user_ = User.query.filter_by(username=username).first()

        if not first_name:
            error = 'First Name cannot be empty'
        elif not last_name:
            error = 'Last Name cannot be empty'
        elif not username:
            error = 'Username cannot be empty'
        elif not email:
            error = 'Email cannot be empty'
        elif user_ is not None:
            error = f'Username {user_.username} is already registered. Create a new one.'
        
        if error is None:
            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
                )
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('login.login'))

        flash(error)

    return render_template('auth/register.html')