import pydantic
from typing import Dict
from pydantic import BaseModel
from utils.exception import APIException


class BaseModelExtend(BaseModel):
    """
        基于pydantic的BaseModel的一个扩展，主要是增加了validation_error异常的捕获处理
    """

    def __init__(self, **data: Dict):
        try:
            super(BaseModelExtend, self).__init__(**data)
        except pydantic.error_wrappers.ValidationError as e:
            raise APIException.ValidationError(e.json())
