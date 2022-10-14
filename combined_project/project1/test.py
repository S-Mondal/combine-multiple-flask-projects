from flask import Blueprint, jsonify

test_api = Blueprint('test',__name__)

@test_api.route("/test")
def test():
	return jsonify({"message":"Hello, Project1"})