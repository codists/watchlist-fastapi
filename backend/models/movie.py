from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Movie(Model):
    """
    The User Model
    """
    name = fields.CharField(max_length=128, null=False, description='电影名')
    year = fields.CharField(max_length=128, null=False, description='电影年份')


