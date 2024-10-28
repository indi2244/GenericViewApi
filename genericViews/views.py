from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import response,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    student=Student.objects.all()
    serializer=StudentSerializer(student , many=True)

    return Response(serializer.data)

@api_view(['GET'])
def student_by_id(request,id):
    try:
        student=Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response (serializer.data, status= status.HTTP_201_CREATED)
    else:
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update(request, id):
    try:
        student=Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    serializer=StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response (serializer.data)
    else:
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)

