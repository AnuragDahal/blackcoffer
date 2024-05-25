from marshmallow import Schema, fields, post_load, EXCLUDE
from datetime import datetime


class IntegerOrString(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if value == "":
            return None
        try:
            return int(value)
        except ValueError:
            return value


class DateTimeOrString(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if value == "":
            return None
        try:
            return datetime.strptime(value, "%B, %d %Y %H:%M:%S")
        except ValueError:
            return value


class ReportSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    end_year = IntegerOrString()
    intensity = IntegerOrString()
    sector = fields.Str()
    topic = fields.Str()
    insight = fields.Str()
    url = fields.Str()
    region = fields.Str()
    start_year = IntegerOrString()
    impact = IntegerOrString()
    added = DateTimeOrString()
    published = DateTimeOrString()
    country = fields.Str()
    relevance = IntegerOrString()
    pestle = fields.Str()
    source = fields.Str()
    title = fields.Str()
    likelihood = IntegerOrString()
