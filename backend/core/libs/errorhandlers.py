from flask import jsonify
from core.server import app


@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': str(error)}), 400


@app.errorhandler(401)
def unauthorized_error(error):
    return jsonify({'error': str(error)}), 401


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': str(error)}), 404


@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({'error': str(error)}), 422
