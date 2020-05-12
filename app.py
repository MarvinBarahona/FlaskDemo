import config
from flask import request

import json

from errors.ValidationError import ValidationError
from models.Saludo import Saludo
from schemas.SaludoSchema import saludo_schema
from requests.SaludoRequest import saludo_request

app = config.app
parser = config.parser


# Routes.
@app.route('/saludo')
def hello_world():
    try:
        args = parser.parse(saludo_request, request,location="query")
        saludo = Saludo(args["nombre"])

        return saludo_schema.dump(saludo)
    except ValidationError as error:
        return json.dumps(error.__str__())


if __name__ == '__main__':
    app.run(debug=True)
