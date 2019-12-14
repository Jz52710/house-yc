from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from housedata.housedata import model

# Create your views here.

def index(request):
    return HttpResponse("hello world")


class Price(APIView):
    def get(self,request,*args,**kwargs):
        cs = model.predict([[1,0,0,0,0,0,1,1,0,46.09,1,0]])[0][0]#测试数据
        return Response({'code':200,'data':int(cs)})

    def post(self,request,*args,**kwargs):
        if request.data['subway'] == '是':
            request.data['subway'] = 1
        else:
            request.data['subway'] = 0
        if request.data['school'] == '是':
            request.data['school'] = 1
        else:
            request.data['school'] = 0

        data = model.predict([[int(request.data['city']),int(request.data['proper']),0,0,0,0,int(request.data['floors']),int(request.data['roomnum']),int(request.data['halls']),int(request.data['area']),int(request.data['subway']),int(request.data['school'])]])
        print(request.data['subway'])

        return Response({'code':200,'data':int(data)})
