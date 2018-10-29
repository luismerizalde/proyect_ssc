from django.shortcuts import render
from django.shortcuts import (get_list_or_404, get_object_or_404,
    render_to_response, HttpResponse, HttpResponseRedirect, redirect
)
from .models import Entidad, Prueba
import json

# Create your views here.

def test_form(request):
	plantilla = "test_form.html"
	return render(request, plantilla)

def vistas_tabla(request):
	if request.method == "POST":
		respuesta = {}
		if request.is_ajax():
			if request.POST['tipo'] == "cargar":
				item = Entidad.objects.get(id = request.POST['item'])
				respuesta['nombre'] = item.nombre
				respuesta['obs'] = item.observacion
				respuesta['mensaje'] = "Datos cargados exitosamente"
				return HttpResponse(json.dumps(respuesta), content_type ="application/json")
		else:
			respuesta['error'] = "Error en la peticion ajax"
			return HttpResponse(json.dumps(respuesta), content_type ="application/json")

def basic_view(request):
	plantilla = "first.html"
	return render(request, plantilla)

def table_esui (request): 
	print("entro tabla")
	plantilla = "tabla.html"
	entidades = Entidad.objects.all()
	return render(request, plantilla, locals())

from .tasks import *
from celery import uuid
def correo_celery(request):
	task_id = uuid()
	# print "el ID de la tarea es:" + task_id
	# send_email_user.delay() 
	fecha = datetime.datetime.now()
	fecha = fecha + datetime.timedelta(minutes=2)
	# print fecha.hour
	# print fecha.minute
	fecha = fecha.strftime('%Y-%m-%d %H:%M')
	print (fecha)
	send_email_user.apply_async(task_id=task_id, args=[task_id, 'test', fecha])
	return HttpResponse('se envio correo correctamente')

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from aplicaciones.modulo1.serializers import UserSerializer, GroupSerializer, EntidadSerializer, EntidadSerializer2, PruebaSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EntidadViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Entidad.objects.all()
	serializer_class = EntidadSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework import status

class EntidadViewSet2(APIView):
	def get(self, request):
		factory = APIRequestFactory()
		request = factory.get('/')
		serializer_context = {
		    'request': Request(request),
		}
		todos = Entidad.objects.all()
		serializer = EntidadSerializer2(todos, many=True, context=serializer_context)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		print('entro peticion delete')
		todo = get_object_or_404(Entidad, pk=pk)
		print(todo)
		todo.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)

	def put(self, request):
		serializer = EntidadSerializer2(data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PruebaViewSet(APIView):
	print('Entro prueba')
	def get(self, request):
		factory = APIRequestFactory()
		request = factory.get('/')
		serializer_context = {
		    'request': Request(request),
		}
		todos = Prueba.objects.all()
		serializer = PruebaSerializer(todos, many=True, context=serializer_context)
		return Response(serializer.data)

	def put(self, request):
		print("ENTRO PUT PRUEBA")
		serializer = PruebaSerializer(data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
