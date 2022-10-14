from flask import Blueprint, render_template
from project1.test import test_api

project1 = Blueprint('project1',__name__, url_prefix='/project1')
project1.register_blueprint(test_api)

@project1.route('/')
def index():
	return render_template("project1/index.html")
