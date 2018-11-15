from flask import render_template, request, current_app

from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    current_app.logger.error('Page not found: %s', request.path)
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    current_app.logger.error('Server Error: %s', error)
    bp.db.session.rollback()
    return render_template('errors/500.html'), 500


@bp.app_errorhandler(Exception)
def unhandled_exception(e):
    current_app.logger.error('Unhandled Exception: %s', e)
    return render_template('errors/500.html'), 500
