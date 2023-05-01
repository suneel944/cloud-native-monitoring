import os
from flask import Blueprint, send_from_directory, current_app



scripts_bp = Blueprint("scripts", __name__)

@scripts_bp.route("/static/js/index.js", methods=["GET"])
def load_scripts():
    return send_from_directory(os.path.join(current_app.root_path, "static/js"), "index.js")