from mongoengine import Document, fields


class Posts(Document):
    source = fields.DictField(null=True)
    author = fields.StringField(null=True)
    title = fields.StringField(null=True)
    description = fields.StringField(null=True)
    url = fields.StringField(null=True)
    urlToImage = fields.StringField(null=True)
    publishedAt = fields.DateTimeField(null=True)
    content = fields.StringField(null=True)
