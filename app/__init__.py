from flask import Flask
from .config import settings

# Flask
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(settings)

# Blueprints
from .views import home
app.register_blueprint(home.home_bp)

from .views import predict
app.register_blueprint(predict.predict_bp)