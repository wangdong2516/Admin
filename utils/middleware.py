from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from collections import defaultdict
import json
import logging

from rest_framework.request import Request

request_log = logging.getLogger('django.request')
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
        drf_request = Request(request)
        data = defaultdict(list)
        for key, value in drf_request.query_params.items():
            data[key] = value
        request.query_params = data
        # request_log.info(
        #     f"path: {request.path}, method:{request.method}, view_name: {request.resolver_match.view_name},"
        #     f"query_params: {request.query_params}, body: {drf_request.data}"
        # )


class ValidationErrorMiddleware(MiddlewareMixin):

    def process_exception(self, *args, **kwargs):
        """
            处理由pydantic抛出的验证错误，并且返回错误信息，错误代码统一为400
        """
        request = args[0]
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
                request_log.error(
                    f"path: {request.path}, method:{request.method}, view_name: {request.resolver_match.view_name},"
                    f"query_params: {request.query_params}, body: {request.body}, response: {response}"
                )
                return JsonResponse(data=response, status=400)
