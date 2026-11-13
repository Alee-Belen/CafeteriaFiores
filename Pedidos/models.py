from django.db import models
from django.conf import settings

# Create your models here.

class Pedido(models.Model):

    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En preparación', 'En preparación'),
        ('Listo', 'Listo'),
        ('Entregado', 'Entregado'),
    ]

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='pedidos'
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    hora_retiro = models.TimeField()

    estado = models.CharField(
        max_length=15,
        choices=ESTADOS,
        default='Pendiente'
    )

    total = models.IntegerField()

    observacion = models.TextField(
        blank=True
    )

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.username}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha']


class DetallePedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles'
    )

    producto = models.ForeignKey(
        'Cafeteria.Producto',
        on_delete=models.PROTECT,
        related_name='detalles'
    )

    cantidad = models.IntegerField()

    precio_unitario = models.IntegerField()

    subtotal = models.IntegerField()

    def __str__(self):
        return f'{self.producto.nombre} x {self.cantidad}'

    class Meta:
        verbose_name = 'Detalle del pedido'
        verbose_name_plural = 'Detalles de pedidos'

        constraints = [
            models.UniqueConstraint(
                fields=['pedido', 'producto'],
                name='pedido_producto_unico'
            )
        ]