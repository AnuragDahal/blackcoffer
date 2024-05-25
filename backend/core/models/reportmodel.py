from core import db


class EnergyReport(db.Model):
    __tablename__ = 'energy_reports'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    end_year = db.Column(db.Integer, default=None)
    intensity = db.Column(db.Integer, default=None)
    sector = db.Column(db.String(500), default=None)
    topic = db.Column(db.String(500), default=None)
    insight = db.Column(db.String(500), default=None)
    url = db.Column(db.String(500), default=None)
    region = db.Column(db.String(50), default=None)
    start_year = db.Column(db.String(50), default=None)
    impact = db.Column(db.Integer, default=None)
    added = db.Column(db.DateTime, default=None)
    published = db.Column(db.DateTime, default=None)
    country = db.Column(db.String(50), default=None)
    relevance = db.Column(db.Integer, default=None)
    pestle = db.Column(db.String(200), default=None)
    source = db.Column(db.String(200), default=None)
    title = db.Column(db.String(500), default=None)
    likelihood = db.Column(db.Integer, default=None)
