from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import TestcalcSerializer
from .models import Testcalc
from django.http import JsonResponse
import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = 'vydehi9'
DATABASE = 'testing'
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

@api_view(['GET'])
def get(request, _num):
    _mar = Testcalc.objects.filter(number = _num)
    if _mar:
        serializer = TestcalcSerializer(_mar, many = True)
        return Response(serializer.data)
    else:
        _sq = int(_num) * int(_num)
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO Details_testcalc  (number, square) values(%s, %s)',(float(_num),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': "New number and it's square inserted", 'Number': _num, 'Square': _sq})




@api_view(['GET'])
def post(request, _values):
    _num, _sq = _values.split('-')
    _mar = Testcalc.objects.filter(number = _num)
    if _mar:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('UPDATE Details_testcalc  SET square = %s WHERE number = %s',(float(_sq),float(_num)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'Square of the given number is updated', 'Number': _num, 'Square': _sq})
    else:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO Details_testcalc  (number, square) values(%s, %s)',(float(_num),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'New number and square inserted', 'Number': _num, 'Square': _sq})
