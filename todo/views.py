from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from provider.oauth2.models import Client

# TODO app
from todo.serializers import RegistrationSerializer
from todo.serializers import UserSerializer, TodoSerializer
from todo.models import Todo

class RegistrationView(APIView):
      permission_classes = ()
    
      def post(self, request):
          serializer = RegistrationSerializer(data=request.DATA)

          if not serializer.is_valid():
             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
 
          data = serializer.data
          # User creation
          u = User.objects.create(username=data['username'])
          u.set_password(data['password'])
          u.save()

          name = u.username
          client = Client(user=u,name=name,url='' + name,client_id=name, client_secret='',client_type=1)
          client.save()

          return Response(serializer.data,status=status.HTTP_201_CREATED)
       

class TodosView(APIView):
      permission_classes = (IsAuthenticated,) 

      def get(self, request):
          todos = Todo.objects.filter(owner=request.user.id)
          serializer = TodoSerializer(todos, many=True)
          return Response(serializer.data)

      def post(self,request):
          serializer = TodoSerializer(data = request.DATA)
          if not serializer.is_valid():
             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
          else:
             data = serializer.data
             owner = request.user
             t = Todo(owner=request.user, description=data['description'],done=False)
             t.save()
             request.DATA['id'] = t.pk;
             return Response(request.DATA,status=status.HTTP_201_CREATED)

      def put(self,request,todo_id):
          serializer = TodoSerializer(data=request.DATA)
          if not serializer.is_valid():
             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
          else:
             data = serializer.data
             desc = data['description']
             done = data['done']
             t = Todo(id=todo_id,owner=request.user,description=desc,done=done,updated=datetime.now())
             t.save()
             return Response(status=status.HTTP_200_OK)
