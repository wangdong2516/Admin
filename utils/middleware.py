import redis
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from collections import defaultdict
import json
import logging

from rest_framework.request import Request
from utils.exception import APIException


request_log = logging.getLogger('django.request')

# 创建redis连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=10, db=1)


class ConvertGetMiddleware(MiddlewareMixin):
    """
        实现全量日志记录
    """

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
            在进入视图函数之前被调用
            针对查询参数的处理，因为查询参数可能存在两种情况
                1. 单个key，单个value
                2. 多个key，多个value
        """
        drf_request = Request(
            request=request
        )
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


# class PVMiddleware(MiddlewareMixin):
#     """
#         网站流量统计中间件，记录响应成功的数量
#     """
#
#     def process_response(self, request, response):
#
#         if response.status_code == 200:
#
#             # 获取一个redis连接,写入访问数
#             connection = redis.Redis(db=1, connection_pool=pool)
#             connection.setnx('visit_num', 0)
#             connection.incr('visit_num', 1)
#
#         return response


class PVMiddleware:

    def __init__(self, get_response):
        """
            初始化
        :param get_response:下一个中间件或者是视图函数
        """
        self.get_response = get_response

    def __call__(self, request):
        """
            实现调用逻辑
        :param request: 请求对象
        :return:
        """

        # 在视图函数处理之前的逻辑
        response = self.get_response(request)

        # 在视图函数处理之后的逻辑
        if response.status_code == 200:
            # 获取一个redis连接,写入访问数
            connection = redis.Redis(db=1, connection_pool=pool)
            connection.setnx('visit_num', 0)
            connection.incr('visit_num', 1)

        return response
