from core import db
import json
from core.models.schemas import ReportSchema
from core.models.reportmodel import EnergyReport as Report



def load_into_db():

    with open("C:\\Users\\freef\\Desktop\\Code playground\\Intern\\blackcoffer\\backend\\jsondata.json", encoding='utf-8') as jsondata:
        data_sample = json.load(jsondata)
    for data in data_sample:
        data_of_energy_reports = ReportSchema().load(data)
        model_of_energy_reports = Report(**data_of_energy_reports)
        db.session.add(model_of_energy_reports)

    db.session.commit()



