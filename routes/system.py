import json
import os
from flask import Blueprint, jsonify, render_template, current_app, send_from_directory

system_bp = Blueprint("system", __name__)


@system_bp.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@system_bp.route("/")
def index():
    return render_template("index.html")


@system_bp.route("/docs")
def docs():
    return render_template("docs.html")


@system_bp.route("/openapi.json")
def openapi_spec():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return send_from_directory(root, "openapi.json", mimetype="application/json")
