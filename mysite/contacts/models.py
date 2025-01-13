from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(verbose_name='Sujeito',max_length=100)
    message = models.CharField(verbose_name='Mensagem',max_length=250)
    sender = models.EmailField(verbose_name='E-mail')
    cc_myself = models.BooleanField(null=True, blank=True, verbose_name="Enviar cópia para mim")