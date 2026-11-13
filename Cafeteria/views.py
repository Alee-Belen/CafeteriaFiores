from django.shortcuts import render
from .models import Producto, Categoria


def catalogo(request):

    productos = Producto.objects.filter(
        disponible=True,
        stock__gt=0,
        categoria__activa=True
    )

    categorias = Categoria.objects.filter(activa=True)

    busqueda = request.GET.get('buscar', '')
    categoria_id = request.GET.get('categoria', '')

    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    contexto = {
        'productos': productos,
        'categorias': categorias,
        'busqueda': busqueda,
        'categoria_seleccionada': categoria_id,
    }

    return render(request, 'catalogo.html', contexto)