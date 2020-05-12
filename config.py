from flask import Flask
from flask_marshmallow import Marshmallow
from webargs import flaskparser
from errors.ValidationError import ValidationError

parser = flaskparser.FlaskParser()


@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise ValidationError(error.messages)


app = Flask(__name__)
ma = Marshmallow(app)
