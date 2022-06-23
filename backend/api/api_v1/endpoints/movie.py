from typing import List, Any, Union

from fastapi import APIRouter, Depends
from core import deps
from schemas import Movie_Pydantic, MovieIn_Pydantic, Response200, Response400
from models import Movie

movie = APIRouter(tags=["电影"])


# 查
@movie.get("/movie", summary="电影列表", response_model=Union[Response200, Response400])
async def movie_list(limit: int = 12, page: int = 1):
    """

    :param limit: 每页显示的条数，默认显示10条/页
    :param page: 第几页，默认第一页
    :return:
    """
    # 分页
    # return await Movie_Pydantic.from_queryset(Movie.all())
    skip = (page - 1) * limit
    data = {
        'total': await Movie.all().count(),
        'movies': await Movie_Pydantic.from_queryset(Movie.all().offset(skip).limit(limit))
    }
    return Response200(data=data)


# 增
@movie.post("/movie", summary="新增电影")
async def movie_create(movie_form: MovieIn_Pydantic, token: Any = Depends(deps.get_current_user)):
    """
    1.目前是只要用户登录了就可以添加电影
    2.添加成功就返回成功的的标志，目前没有失败的情况
    :param movie_form: movie
    :param token: token
    :return:
    """
    return Response200(data=await Movie_Pydantic.from_tortoise_orm(await Movie.create(**movie_form.dict())))


# 改
@movie.put("/movie/{pk}", summary="编辑电影")
async def movie_update(pk: int, movie_form: MovieIn_Pydantic, token: Any = Depends(deps.get_current_user)):
    if await Movie.filter(pk=pk).update(**movie_form.dict()):
        return Response200()
    return Response400(msg="更新失败")


# 删除
@movie.delete("/movie/{pk}", summary="delete movie")
async def movie_delete(pk: int, token: Any = Depends(deps.get_current_user)):
    if await Movie.filter(pk=pk).delete():
        return Response200()

    return Response400({'msg': '删除失败'})
