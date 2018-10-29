from celery import shared_task, result, task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
import time
from proyecto.celery import app
import datetime


@shared_task
def send_email_user(id,args,fecha):
	# print fecha
	# print id
	asunto = 'mensaje de prueba'
	mensaje = 'Bienvenido, esto es un mensaje de prueba CELERY'
	users = User.objects.filter(id = 1)
	# users = User.objects.all()

	flg = False
	while flg == False:
		
		time.sleep(15)
		fecha_ahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		if fecha_ahora == fecha:
			print ("ENTRO ENVIAR CORREO")	
			print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))	
			# revocar_tarea(id)
			for x in users:
				send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [x.email], fail_silently = False)
			flg = True
	print ("Salio WHILE")


from billiard.exceptions import Terminated
@task(throws=(Terminated,))
def revocar_tarea(id):
	print ("entro tarea revocar")
	try:
		app.control.revoke(id, terminate=True)
	except Terminated:
		pass	
	return "tarea terminada con exito"
	# result.AsyncResult(id).revoke()