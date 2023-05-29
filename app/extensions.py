from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_migrate import Migrate

migrate = Migrate()

from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

UserMixin = UserMixin

login_user = login_user

login_manager = LoginManager()

login_required = login_required

logout_user = logout_user

current_user = current_user

