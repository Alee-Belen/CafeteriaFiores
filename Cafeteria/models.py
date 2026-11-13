from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(
        max_length=50,
        unique=True
    )

    descripcion = models.TextField(
        blank=True
    )

    activa = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']


class Producto(models.Model):

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos'
    )

    codigo = models.CharField(
        max_length=10,
        unique=True
    )

    nombre = models.CharField(
        max_length=100
    )

    precio = models.IntegerField()

    stock = models.IntegerField()

    disponible = models.BooleanField(
        default=True
    )

    creado = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']