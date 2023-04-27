import os
from flask import Blueprint, send_from_directory


css_bp = Blueprint("css", __name__)

@css_bp.route("/static/css/index.css", methods=["GET"])
def set_css():
    from app import app
    return send_from_directory(os.path.join(app.root_path, "static/css"), "index.css")