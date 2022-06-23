# save settings which are not change
import secrets
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    DESC: Optional[str] = '''
    movie list implemented by FastAPI
    '''

    TITLE: Optional[str] = '''
    movie list API
    '''
    ALGORITHM: str = "HS256"  # 加密算法
    # 随机生成的base64位字符串,后端重启后token会失效，不方便测试，所以测试的时候SECRET_KEY最好改成固定的
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3

    # 跨域
    ORIGINS = [
        'http://localhost:3000',
        'http://127.0.0.1:3000',
        'http://127.0.0.1:8000',
        'http://localhost:8000',
        '*',
    ]


settings = Settings()




