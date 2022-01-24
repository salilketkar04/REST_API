from rest_framework import generics
from rest_framework.response import Response
from .serializer import GamesSerializer
from .models import Games


class GamesCreateApi(generics.CreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class GamesListApi(generics.ListAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class GamesUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class GamesDeleteApi(generics.RetrieveDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
