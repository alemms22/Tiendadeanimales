from django.db import models

# Create your models here.
class partner(models.Model):
    name=models.CharField(max_lenght=50,help_text='Escriba el nombre del proveedor')
    tel = models.CharField(max_lenght=12,help_text='Escriba el numero del proveedor')
    email = models.EmailField(help_text='Ingrese el email de contacto del proveedor')
    startre= models.DateField(help_text='Seleccione la fecha de inicio de relación con el proveedor')

class product(models.Model):
    Product = models.CharField(max_lenght=40,help_text='Escriba el nombre del producto')
    Parner = models.ForeignKey(partner)
    Clasificacition = models.CharField(max_lenght=40,help_text='Escriba la Clasificacicion')
    Date = models.DateField(auto_now=True)

class comida(models.Model):
    
