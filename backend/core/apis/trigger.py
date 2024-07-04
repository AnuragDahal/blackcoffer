from flask import Blueprint, jsonify, current_app
from core.libs import loadintodb
from core import db

trigger = Blueprint('trigger', __name__)


@trigger.route('/triggerdb', methods=['POST'], strict_slashes=False)
def triggerdb():

    with current_app.app_context():
        db.create_all()
        isLoaded = loadintodb.load_into_db()
        if isLoaded:
            return jsonify({"message": "Data loaded successfully"}), 200
        else:
            return jsonify({"message": "Data loading failed"}), 500
