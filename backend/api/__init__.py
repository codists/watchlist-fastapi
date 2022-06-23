"""
create app
"""
import logging
import sys

from fastapi import FastAPI, applications
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from fastapi.openapi.docs import get_swagger_ui_html  #

from .api_v1 import v1
from core import settings

app = FastAPI(description=settings.DESC, title=settings.TITLE)
app.include_router(v1, prefix='/api')


# 解决swagger文档加载不出来的问题
def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui-bundle.js',
        swagger_css_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui.css'
    )


applications.get_swagger_ui_html = swagger_monkey_patch

# # 设置formatter
# fmt = logging.Formatter(
#     fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )
#
# # 设置handler
# sh = logging.StreamHandler(sys.stdout)
# sh.setLevel(logging.DEBUG)
# sh.setFormatter(fmt)
#
# # 设置logger1
# logger_db_client = logging.getLogger('tortoise.db_client')
# logger_db_client.setLevel(logging.DEBUG)
# logger_db_client.addHandler(sh)
#
# # 设置logger2
# logger_tortoise = logging.getLogger('tortoise')
# logger_tortoise.setLevel(logging.DEBUG)
# logger_tortoise.addHandler(sh)

register_tortoise(
    app,
    db_url='sqlite://watchlist.sqlite',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

