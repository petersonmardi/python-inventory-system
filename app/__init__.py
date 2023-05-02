from flask import Flask
from .extensions import db, migrate
import os

def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)


    app.config.from_mapping(
        SECRET_KEY = 'development',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///db_inventory.db',
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
    )

    db.init_app(app)

    migrate.init_app(app, db)


    with app.app_context():
        db.create_all()
        print("Initialized database...")

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/hello')
    def hello():
        return "Hello, this an inventory system!"

    from .routes.create_item import create_bp
    app.register_blueprint(create_bp)
    
    from .routes.index import index_bp
    app.register_blueprint(index_bp)

    from .routes.update_item import update_item_bp
    app.register_blueprint(update_item_bp)

    from .routes.delete_item import delete_bp
    app.register_blueprint(delete_bp)


    return app

create_app()