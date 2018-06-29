from rest_framework import serializers
from .models import Testcalc

class TestcalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcalc
        fields = ('number', 'square')


#serializers usd to convert the data from Json format
