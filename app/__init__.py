from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#Create a bootstrap instance
bootsrap = Bootstrap()

def create_app(config_name):
    
    app = Flask(__name__)
    
    #Create tha app configurations
    app.config.from_object(config_options[config_name])
    
    # Initializing flask extensions
    bootsrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)
 
    # from app import views
    # from app import errors
    
    return app

