'''
This file has the scope of release the views at the moment
when there are errors within the application.
'''
from flask import render_template

from . import main


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('main/error.html', error_code=403, error_msg="Access Denied"), 403

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('main/error.html', error_code=404, error_msg="Page not found"), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('main/error.html', error_code=500, error_msg="Internal server error"), 500