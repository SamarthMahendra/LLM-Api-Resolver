from django.shortcuts import render

# import Apiviews
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


# add TO Todo model
from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
@api_view(['GET'])
def TodoDetail(request):
    pk = request.GET.get('pk', None)
    if pk:
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def TodoPost(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view['PUT']
def TodoPut(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view['DELETE']
def TodoDelete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return Response(status=204)




