from webargs import fields


saludo_request = {
    "nombre": fields.Str(required=False, missing="")
}