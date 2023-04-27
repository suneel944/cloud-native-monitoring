import os
from flask import Blueprint, url_for, send_from_directory



scripts_bp = Blueprint("scripts", __name__)

@scripts_bp.route("/static/js/index.js", methods=["GET"])
def load_scripts():
    from app import app
    return send_from_directory(os.path.join(app.root_path, "static/js"), "index.js")