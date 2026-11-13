from django.contrib import admin
from .models import Pedido, DetallePedido


class DetallePedidoInline(admin.TabularInline):

    model = DetallePedido

    extra = 0

    readonly_fields = (
        'producto',
        'cantidad',
        'precio_unitario',
        'subtotal'
    )


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'cliente',
        'fecha',
        'hora_retiro',
        'estado',
        'total'
    )

    search_fields = (
        'cliente__username',
        'cliente__first_name'
    )

    list_filter = (
        'estado',
        'fecha'
    )

    inlines = [DetallePedidoInline]


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):

    list_display = (
        'pedido',
        'producto',
        'cantidad',
        'precio_unitario',
        'subtotal'
    )

    search_fields = (
        'producto__nombre',
    )