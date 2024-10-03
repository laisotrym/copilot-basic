from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize the database
    db.init_app(app)
    migrate.init_app(app, db)

    # Register the blueprints / url
    from app.user.controller import user_bp
    app.register_blueprint(user_bp, url_prefix='/api')

    return app