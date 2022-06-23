from typing import Iterable, Optional

from tortoise import BaseDBAsyncClient, fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

from core import get_password_hash


class User(Model):
    """
    The User Model
    """
    username = fields.CharField(max_length=20, null=False, description='用户名')
    password = fields.CharField(max_length=128, null=False, description='密码')
    nickname = fields.CharField(max_length=20, null=True, description='昵称', default='')

    async def save(
            self,
            using_db: Optional[BaseDBAsyncClient] = None,
            update_fields: Optional[Iterable[str]] = None,
            force_create: bool = False,
            force_update: bool = False,
    ) -> None:
        # hash password
        if force_create or 'password' in update_fields:
            self.password = get_password_hash(self.password)

        await super(User, self).save(using_db, update_fields, force_create, force_update)
