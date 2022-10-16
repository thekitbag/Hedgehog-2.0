from ensurepip import bootstrap
from flask import Flask
from config import Config

from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bootstrap.init_app(app)

    from webapp.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app