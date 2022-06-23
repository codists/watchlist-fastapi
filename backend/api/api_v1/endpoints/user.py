from typing import Any, Optional, List

from fastapi import APIRouter, Depends

from core import deps
from schemas import User_Pydantic, UserIn_Pydantic
from models import User
from schemas import Response200, Response400

# 路由全局设置都要认证,而不是设置到某个方法上
# user = APIRouter(tags=["user info"], dependencies=[Depends(deps.get_current_user)])
user = APIRouter(tags=["user info"])


@user.get("/user", summary="current user")
async def user_info(user_obj: Any = Depends(deps.get_current_user)):
    return Response200(data=await User_Pydantic.from_tortoise_orm(user_obj))


@user.put("/user", summary="更新用户信息")
async def user_update(user_form: UserIn_Pydantic, user_obj: User = Depends(deps.get_current_user)):
    # 因为有些字段可能不需要修改，所以不能给update()传递**user_form.dict()，不然某些没有传值的字段就会被设置为空
    if await User.filter(username=user_obj.username).update(nickname=user_form.nickname):
        return Response200(data=await User_Pydantic.from_tortoise_orm(user_obj))
    return Response400(msg="更新失败")


__all__ = ["user"]
