from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render


@login_required
def inicio(request):
    if request.user.is_staff:
        return redirect('panel_encargado')

    return redirect('panel_cliente')


@login_required
def panel_encargado(request):
    if not request.user.is_staff:
        raise PermissionDenied

    return render(request, 'panel_encargado.html')

@login_required
@user_passes_test(lambda usuario: not usuario.is_staff)
def panel_cliente(request):
    return render(request, 'panel_cliente.html')