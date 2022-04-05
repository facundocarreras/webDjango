from django.db import models

class TipoDeporte(models.Model):
    detalle_deporte = models.CharField(max_length = 200) 

class TipoIndumentaria(models.Model):
    detalle_indumentaria = models.CharField(max_length = 200)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length = 200)
    tipo_deporte = models.ForeignKey(TipoDeporte, on_delete=models.CASCADE)
    tipo_indumentaria = models.ForeignKey(TipoIndumentaria, on_delete=models.CASCADE)
    stock = models.IntegerField(max_length = 11)


