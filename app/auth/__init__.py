from flask import Blueprint


auth = Blueprint('auth',_name)

from . import views, forms