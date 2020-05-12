import config
from models.Saludo import Saludo
from schemas.SaludoSchema import saludo_schema
from webargs.flaskparser import use_args
from requests.SaludoRequest import saludo_request

app = config.app


# Routes.
@app.route('/saludo')
@use_args(saludo_request, location="query")
def hello_world(args):
    saludo = Saludo(args["nombre"])
    return saludo_schema.dump(saludo)


if __name__ == '__main__':
    app.run()
