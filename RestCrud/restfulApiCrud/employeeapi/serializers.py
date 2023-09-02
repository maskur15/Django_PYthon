# api <> web_app/ mobile app
# python_represnentation <> JSON/ xml
#serializer use to convert json to python representation and vice versa
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields = '__all__'