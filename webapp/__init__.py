from ensurepip import bootstrap
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
import posthog

posthog.project_api_key = 'phc_UZILuAviYkk13s70pSY0JcMHvFNNPAxvBnS8loD3PCG'
posthog.personal_api_key = 'phx_PJ7n5HJQpcveKM3lMBRthZtrVPo7bEdwiR4rYsmifAB'


bootstrap=Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bootstrap.init_app(app)

    from webapp.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
