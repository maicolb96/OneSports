from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
# Create your models here.
objeto = ''
def nombreImagen(instance, filename):
    extension = os.path.splitext(filename)[1]
    new_filename = f"{uuid4().hex}{extension}"
    return os.path.join(objeto, new_filename)

class Relation(models.Model):
    current_user = models.ForeignKey(User,related_name='current_user',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Relation'

class Post(models.Model):
    global objeto
    object = 'post'
    image = models.ImageField(upload_to=nombreImagen,null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True,help_text='Cuerpo de la publicacion')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'post'
        
class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'likes'
        
class Comments(models.Model):
    comentario = models.TextField(help_text='Comentario del post')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Comments'
    
class Events(models.Model):
    global objeto
    object = 'event'
    title = models.CharField(max_length=155,help_text='Titulo del evento')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(null=False,blank=False,help_text='Cuerpo del evento')
    fecha = models.CharField(max_length=25,help_text='Fecha del evento')
    hora = models.CharField(max_length=25,help_text='Hora del evento')
    image = models.ImageField(upload_to=nombreImagen,null=True,blank=True)
    lugar = models.CharField(max_length=255,help_text='Lugar del evento')

    class Meta:
        db_table = 'Events'
