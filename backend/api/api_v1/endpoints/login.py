from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from core import verify_password, create_access_token
from models import User
from schemas import UserIn_Pydantic, Response200, Response400, ResponseToken, User_Pydantic

login = APIRouter(tags=["登录"])


@login.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    this use form_data
    :param form_data:
    :return:
    """

    # determine whether username exist
    if user := await User.get(username=form_data.username):
        if verify_password(form_data.password, user.password):
            # return must be this format
            token = create_access_token({'sub': user.username})
            return ResponseToken(data={'token': f'bearer {token}'}, access_token=token)
    return Response400(msg='username or password error')


@login.post('/user', summary='create user')
async def create_user(user: UserIn_Pydantic):
    if await User.filter(username=user.username):
        return Response400(msg="用户已存在.")
    return Response200(
        data=await User_Pydantic.from_tortoise_orm(await User.create(**user.dict()))
    )
