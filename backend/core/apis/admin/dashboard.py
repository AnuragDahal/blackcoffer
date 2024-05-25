from flask import Blueprint, request, abort
from core.libs.responses import APIResponse
from core.models.reportmodel import EnergyReport
from core.models.schemas import ReportSchema
from urllib.parse import unquote
import random

admin_dashboard = Blueprint('admin_dashboard', __name__)


@admin_dashboard.route('/endyear', methods=['GET'], strict_slashes=False)
def filter_for_end_year():

    # Retrieve the end year from the query parameters
    end_year = request.args.get('end_year')
    # Query the database for all the records
    if not end_year:
        abort(400, 'End year is required')
    reports_for_end_year = EnergyReport.query.filter_by(
        end_year=end_year).all()
    reports_for_end_year_dump = ReportSchema(
        many=True).dump(reports_for_end_year)
    return APIResponse.respond(data=reports_for_end_year_dump)


@admin_dashboard.route('/topic', methods=['GET'], strict_slashes=False)
def filter_for_topics():

    topic_encoded = request.args.get('topic')

    if not topic_encoded:
        abort(400, 'Topics is required')

    topic = unquote(topic_encoded)

    reports_for_topic = EnergyReport.query.filter_by(topic=topic).all()
    if not reports_for_topic:
        abort(404, 'No reports found for the specified topics')

    reports_for_topic_dump = ReportSchema(
        many=True).dump(reports_for_topic)
    return APIResponse.respond(data=reports_for_topic_dump)


@admin_dashboard.route('/sector', methods=['GET'], strict_slashes=False)
def filter_for_sector():

    sector_encoded = request.args.get('sector')

    if not sector_encoded:
        abort(400, 'Sector is required')

    sector = unquote(sector_encoded)

    reports_for_sector = EnergyReport.query.filter_by(sector=sector).all()
    if not reports_for_sector:
        abort(404, 'No reports found for the specified sector')

    reports_for_sector_dump = ReportSchema(
        many=True).dump(reports_for_sector)
    return APIResponse.respond(data=reports_for_sector_dump)


@admin_dashboard.route('/region', methods=['GET'], strict_slashes=False)
def filter_for_region():

    region_encoded = request.args.get('region')

    if not region_encoded:
        abort(400, 'Region is required')

    region = unquote(region_encoded)
    reports_for_region = EnergyReport.query.filter_by(region=region).all()
    if not reports_for_region:
        abort(404, 'No reports found for the specified region')
    reports_for_region_dump = ReportSchema(many=True).dump(reports_for_region)
    return APIResponse.respond(data=reports_for_region_dump)


@admin_dashboard.route("/pestle", methods=["GET"], strict_slashes=False)
def filter_for_pest():

    pestle_encoded = request.args.get("pestle")

    if not pestle_encoded:
        abort(400, "Pestle is required")

    pestle = unquote(pestle_encoded)

    reports_for_pestle = EnergyReport.query.filter_by(pestle=pestle).all()
    if not reports_for_pestle:
        abort(404, "No reports found for the specified pest")
    reports_for_pestle_dump = ReportSchema(many=True).dump(reports_for_pestle)
    return APIResponse.respond(data=reports_for_pestle_dump)


@admin_dashboard.route("/source", methods=['GET'], strict_slashes=False)
def filter_for_source():

    source = request.args.get("source")

    if not source:
        abort(400, "Source is required")

    reports_for_source = EnergyReport.query.filter_by(source=source).all()
    if not reports_for_source:
        abort(404, "No reports found for the specified source")
    reports_for_source_dump = ReportSchema(many=True).dump(reports_for_source)
    return APIResponse.respond(data=reports_for_source_dump)


@admin_dashboard.route("/country", methods=['GET'], strict_slashes=False)
def filter_for_country():

    country_encoded = request.args.get('country')

    if not country_encoded:
        abort(400, "Country is required")

    country = unquote(country_encoded)

    reports_for_country = EnergyReport.query.filter_by(country=country).all()
    if not reports_for_country:
        abort(404, f"No reports found for the {country} ")
    reports_for_country_dump = ReportSchema(
        many=True).dump(reports_for_country)
    return APIResponse.respond(data=reports_for_country_dump)

@admin_dashboard.route('/random', methods=['GET'], strict_slashes=False)
def get_random_data_from_db():

    # generate a random index from 1 to 1000
    starting_id = random.randint(1, 400)
    ending_id = random.randint(500, 1000)
    random_data = EnergyReport.query.filter(
        EnergyReport.id > starting_id, EnergyReport.id < ending_id).all()
    random_data_dump = ReportSchema(many=True).dump(random_data)
    return APIResponse.respond(data=random_data_dump)