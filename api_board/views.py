from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BoardSerializer
from rest_framework import status
from .models import Board
class BoardView(APIView):
    def post(self, request):
        board_serializer = BoardSerializer(data=request.data)
        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data, status=201)
        else:
            return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            board_queryset = Board.objects.all()
            board_queryset_serializer = BoardSerializer(board_queryset, many=True)
            return Response(board_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id= kwargs.get('id')
            board_serializer = BoardSerializer(Board.object.get(id=id))
            return Response(board_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        return Response("ok", status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        return Response("ok", status=status.HTTP_200_OK)