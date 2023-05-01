import os
from flask import Blueprint, send_from_directory,current_app


css_bp = Blueprint("css", __name__)

@css_bp.route("/static/css/index.css", methods=["GET"])
def set_css():
    return send_from_directory(os.path.join(current_app.root_path, "static/css"), "index.css")