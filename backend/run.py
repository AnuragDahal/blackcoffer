from core.server import app
from core import db
import os
# from core.libs import loadintodb

with app.app_context():
    from core.models.reportmodel import EnergyReport
    db.create_all()
    # loadintodb.load_into_db()

if __name__ == "__main__":
    # os.environ["FLASK_ENV"] = "development"
    # app.run(host='127.0.0.1', port=5000
    #         )

    os.environ["FLASK_ENV"] = "production"
    app.run(host='0.0.0.0', port=5000)
