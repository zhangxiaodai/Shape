#-*-coding:utf-8-*-

from flask import Blueprint

auth_blueprint = Blueprint(
    'auth',
    __name__,
    url_prefix = "/auth"
)

from . import views
