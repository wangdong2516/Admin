class APIException:

    # 数据验证相关的异常
    class ValidationError(Exception):

        code = 10001
        detail = '验证错误'
        status_code = 400

    # 用户模型相关的异常
    class UserException:

        class UserDontExistsError(Exception):
            code = 10002
            detail = '用户不存在'
            status_code = 400
