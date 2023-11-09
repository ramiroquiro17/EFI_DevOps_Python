from app import ma
from marshmallow import fields


class PostSchema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    title = fields.String()
    content = fields.String()
    user = fields.Integer()

    
class UserSchema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    username = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    posts = fields.Nested(PostSchema, many=True)