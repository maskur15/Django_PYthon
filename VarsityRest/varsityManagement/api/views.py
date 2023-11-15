from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import studentSerializer
from student.models import Student
from rest_framework import status

@api_view(['GET'])
def getData(request):
    students = Student.objects.all()
    serializer = studentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = studentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getItem(rquest,id):
    try:
        student= Student.objects.get(pk=id)
        serializer = studentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def deleteItem(request,id):
    try:
        student= Student.objects.get(pk=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
def putItem(request,id):
        student= Student.objects.get(pk=id)
        serializer = studentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)