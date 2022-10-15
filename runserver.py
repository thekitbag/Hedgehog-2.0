import os
from webapp import create_app
import config

if os.environ['FLASK_ENV'] == 'development':
	app = create_app(config.DevelopmentConfig)
elif os.environ['FLASK_ENV'] == 'staging':
	app = create_app(config.StagingConfig)
elif os.environ['FLASK_ENV'] == 'prod':
	app = create_app(config.ProductionConfig)
else:
	print('ENV NOT SET TO dev, staging or prod')