from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/ping", methods=["GET"])
def retrive_health():
    return jsonify({"status": "OK"})