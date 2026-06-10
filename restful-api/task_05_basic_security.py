#!/usr/bin/python3
"""API Security and Authentication"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify basic auth credentials"""
    user = users.get(username)

    if user and check_password_hash(
            user["password"],
            password):
        return username

    return None


@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify(
        {"error": "Missing or invalid token"}
    ), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify(
        {"error": "Invalid token"}
    ), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(
        {"error": "Token has expired"}
    ), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify(
        {"error": "Token has been revoked"}
    ), 401


@jwt.needs_fresh_token_loader
def fresh_token_callback(jwt_header, jwt_payload):
    return jsonify(
        {"error": "Fresh token required"}
    ), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic auth route"""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Generate JWT token"""

    data = request.get_json()

    if not data:
        return jsonify(
            {"error": "Invalid credentials"}
        ), 401

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user:
        return jsonify(
            {"error": "Invalid credentials"}
        ), 401

    if not check_password_hash(
            user["password"],
            password):
        return jsonify(
            {"error": "Invalid credentials"}
        ), 401

    token = create_access_token(
        identity={
            "username": username,
            "role": user["role"]
        }
    )

    return jsonify({
        "access_token": token
    })


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT protected route"""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Admin route"""

    identity = get_jwt_identity()

    if identity["role"] != "admin":
        return jsonify({
            "error": "Admin access required"
        }), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
