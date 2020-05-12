from webargs import fields, validate

saludo_request = {
    "nombre": fields.Str(required=False, missing="", validate=validate.Regexp(r"^[a-zA-Z ]{4,20}$"))
}
