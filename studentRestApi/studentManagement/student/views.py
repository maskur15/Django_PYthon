from django.shortcuts import render
from django.http import JsonResponse
from .models import Student 
from  .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def student_list(request):
    #get all the student 
    #serialize them 
    #return json 
    if request.method=='GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return JsonResponse({'students':serializer.data})
    elif request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= HTTP_201_CREATED)
