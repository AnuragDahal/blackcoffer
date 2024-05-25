from core.apis.admin.dashboard import admin_dashboard
from core import app
from flask_cors import CORS

app.register_blueprint(admin_dashboard, url_prefix='/reports')
CORS(app)

CORS(app, origins="http://localhost:5173")