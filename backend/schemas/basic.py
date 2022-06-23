"""
统一返回格式：
1.返回的格式是怎么样的？
"""
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    """
    业务状态码
    """
    SUCCESS = 200
    FAIL = 400


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description='业务状态码，200表示成功，400表示失败。')
    data: Any = Field(default=None, description='数据结果')
    msg: str = Field(default='请求成功', description='请求结果提示')


class Response200(ResponseBasic):
    pass


class ResponseToken(Response200):
    access_token: str = None,
    token_type: str = Field(default='bearer')


class Response400(ResponseBasic):
    code = CodeEnum.FAIL
    msg = '请求失败'
