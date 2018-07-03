from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import TestcalcSerializer
from .models import Testcalc
from django.http import JsonResponse

@api_view(['GET']) #calling api_view by using decorators with help of GET
def test(request):#TEST The function printing in Json format or not
	return Response({'Everything': 'Fair and Lovely', 'Welcome': 'everybody'})
@api_view(['GET'])

def getlist(request):
    if request.method == 'GET':
        stvalue = Testcalc.objects.all()
        serializer = TestcalcSerializer(stvalue,many=True)
        return Response(serializer.data)
    else:
        return Response("No Data")


@api_view(['POST'])
def add_cal(request):
    number = request.data.get("number", None)
    square = request.data.get("square", None)
    cal = Testcalc.objects.create(number=number,square=square)
    return Response({'message' : 'Square updated or created'})
