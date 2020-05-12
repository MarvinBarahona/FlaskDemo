from config import ma


class SaludoSchema(ma.Schema):
    class Meta:
        fields = ("mensaje", "fecha")


saludo_schema = SaludoSchema()
