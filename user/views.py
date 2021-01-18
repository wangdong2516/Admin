from user.validation import IndexModel
from django.http import JsonResponse
from django.views import View

# Create your views here.


class IndexView(View):

    def get(self, request):
        # request.GET是一个类字典的一个对象，进行参数校验
        index_model = IndexModel(**request.query_params)
        # 获取校验的数据
        data = index_model.dict()
        return JsonResponse({'message': data})