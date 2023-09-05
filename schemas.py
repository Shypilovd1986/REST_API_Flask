from marshmallow import Schema, validate, fields


class english_word_schema(Schema):
    word_id = fields.Integer(dump_only=True)
    word = fields.String(required=True)
    transcription = fields.String(required=True)
    notes = fields.String()
    date_of_adding = fields.String(required=True)
    user_id = fields.Integer(required=True)
