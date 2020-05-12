from config import ma


class SaludoSchema(ma.Schema):
    class Meta:
        fields = ("mensaje", "nombre", "fecha")


saludo_schema = SaludoSchema()
