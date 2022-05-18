from flask import Blueprint, render_template, url_for
from app.forms.form import TweetForm
import requests

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET", "POST"])
def home():
    form = TweetForm()

    if form.validate_on_submit():
        data = {"text": form.tweet.data}
        resp = requests.post(url_for("predict.predict", _external=True), json=data)
        return render_template("index.html", form=form, prediction=resp.json())

    return render_template("index.html", form=form)
