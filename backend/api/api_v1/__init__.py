# 设置版本号
from fastapi import APIRouter
# 等效写法：from .endpoints import login, movie, user
from .endpoints import *

v1 = APIRouter(prefix="/v1")
v1.include_router(login)
v1.include_router(movie)
v1.include_router(user)
