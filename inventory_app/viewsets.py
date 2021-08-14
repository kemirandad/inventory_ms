from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Item
from . import serializers

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()#.order_by('id')
    serializer_class = serializers.ItemSerializer
