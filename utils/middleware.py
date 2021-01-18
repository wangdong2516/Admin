from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from collections import defaultdict
import json

from utils.exception import APIException


class ConvertGetMiddleware(MiddlewareMixin):
    """
        转换GET查询参数为dict的中间件
    """

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
            在进入视图函数之前被调用
            针对查询参数的处理，因为查询参数可能存在两种情况
                1. 单个key，单个value
                2. 多个key，多个value
        """

        data = defaultdict(list)
        for key, value in request.GET.items():
            data[key] = value
        request.query_params = data


class ValidationErrorMiddleware(MiddlewareMixin):

    def process_exception(self, *args, **kwargs):
        """
            处理由pydantic抛出的验证错误，并且返回错误信息，错误代码统一为400
        """
        response = {
            'success': False,
            'info': '',
            'code': None,
            'data': ''
        }
        for arg in args:
            # 只处理pydantic抛出的验证错误
            if isinstance(arg, APIException.ValidationError):
                error_reason = json.loads(arg.args[0])
                code = arg.code
                if error_reason:
                    response.update(info=error_reason)
                if code:
                    response.update(code=code)
                return JsonResponse(data=response, status=400)
