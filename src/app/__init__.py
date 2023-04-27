from flask import Flask, url_for
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    __register_blueprints(app)
    __register_error_handler(app)
    
    return app

def __register_error_handler(app: Flask):
    from src.app.services.Errors import handle_exception
    app.register_error_handler(Exception, handle_exception)

def __register_blueprints(app:Flask):
    from .blueprints.metrics.Metrics import metrics_bp
    from .blueprints.health.Health import health_bp
    from .blueprints.data_stream.Data_Stream import data_stream_bp
    from .blueprints.frontend.favicon.Favicon import favicon_bp
    from .blueprints.frontend.scripts.Scripts import scripts_bp
    
    app.register_blueprint(metrics_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(data_stream_bp)
    app.register_blueprint(favicon_bp)
    app.register_blueprint(scripts_bp)