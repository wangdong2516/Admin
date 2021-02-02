from rest_framework.response import Response


class DRFResponse(Response):

    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        data.update(code=20000)
        super(DRFResponse, self).__init__(
            data=data, status=status, template_name=template_name, headers=headers,
            exception=exception, content_type=content_type
        )
