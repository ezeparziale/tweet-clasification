from flask import Flask
from .config import settings

from .views import home
from .views import predict


# Flask
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(settings)

# Blueprints
app.register_blueprint(home.home_bp)
app.register_blueprint(predict.predict_bp)
