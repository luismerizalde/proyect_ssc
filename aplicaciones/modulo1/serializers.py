from django.contrib.auth.models import User, Group
from .models import Entidad, Prueba
from rest_framework import serializers #,ModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EntidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entidad
        fields = ('id', 'url', 'nombre', 'observacion')

class EntidadSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = ('id', 'url', 'nombre')

class PruebaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Prueba
		fields = ('text', 'estado')