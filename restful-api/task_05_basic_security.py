#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT Configuration
# In production, use an environment variable for the secret key
app.config["JWT_SECRET_KEY"] = "super-secret-key-123"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Mock user database with hashed passwords and roles
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

# --- BASIC AUTHENTICATION SETUP ---

@auth.verify_password
def verify_password(username, password):
    """Verifies the username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

# --- JWT ERROR HANDLERS (Requirement: Always return 401 for auth errors) ---

@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
def handle_auth_errors(err):
    """Ensures all authentication failures return a 401 Unauthorized status."""
    return jsonify({"error": "Missing, invalid or expired token"}), 401

# --- API ENDPOINTS ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates user and returns a JWT token.
    The role is embedded as a custom claim in the token.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Additional claims allow us to store roles inside the encrypted token
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user["role"]}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Role-based Access Control (RBAC).
    Extracts the role from the JWT claims to check for admin privileges.
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run(port=5000)
