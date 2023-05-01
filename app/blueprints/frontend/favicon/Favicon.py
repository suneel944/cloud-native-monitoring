import os
from flask import Blueprint, send_from_directory, current_app


favicon_bp = Blueprint("favicon", __name__)

@favicon_bp.route("/favicon.ico", methods=["GET"])
@favicon_bp.route("/static/favico-16.ico", methods=["GET"])
def favicon():
    """To resolve favicon 500 error and also to add image to the browser tab"""
    return send_from_directory(os.path.join(current_app.root_path, "static"), "favico-16.ico")