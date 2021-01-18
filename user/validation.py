from typing import Optional
from utils.validation import BaseModelExtend


class IndexModel(BaseModelExtend):
    """
        首页视图函数使用的数据验证模型
    """

    name: str
    age: int
    description: Optional[int] = None

