from app import app
from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import JWTManager

from flask_cors import CORS, cross_origin

CORS(app, support_credentials=True)
JWTManager(app)

@app.route("/home", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def home():
	return True
