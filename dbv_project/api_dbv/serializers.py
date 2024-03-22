from .models import DBVUser
from rest_framework import serializers

class DBVUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DBVUser
        fields = {'id', 'username'}