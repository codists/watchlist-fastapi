# 返回
from tortoise.contrib.pydantic import pydantic_model_creator

from models import User

# exclude: 就是不使用该字段，例如将user对象返回给客户端的时候，password属性可以不用返回，
User_Pydantic = pydantic_model_creator(User, name="User", exclude=('password',))

# 参考：https://tortoise.github.io/examples/fastapi.html#main-py
# exclude_readonly=True, 设置exclude_readonly=True，那么在docs那里不显示id
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
