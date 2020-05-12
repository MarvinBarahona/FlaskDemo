import config
from models.Saludo import Saludo
from schemas.SaludoSchema import saludo_schema

app = config.app


# Routes.
@app.route('/saludo')
def hello_world():
    saludo = Saludo()
    return saludo_schema.dump(saludo)


if __name__ == '__main__':
    app.run()
