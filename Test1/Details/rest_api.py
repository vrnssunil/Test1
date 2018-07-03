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
@api_view(['GET', 'POST', 'PUT'])
def post (request,_number):

    if request.method == 'GET':
        mul = Testcalc.objects.filter(number=_number)
        serializer = TestcalcSerializer(mul, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TestcalcSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status= 301)

    elif request.method == 'PUT':
        print (request.data)
        mul = Testcalc.objects.filter(number=request.data["number"])
        print (mul)
        mul.update(square=request.data["square"])
        serializer = TestcalcSerializer(data=mul, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 301)
@api_view(['DELETE'])
def apinum(request,_number):
	print(request.data)
	num = Testcalc.objects.filter(number=_number).delete()
	print (num)
#	num.delete(number=request.data["number"])
	serializer = TestcalcSerializer(data=num, many=True)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status= 301)

