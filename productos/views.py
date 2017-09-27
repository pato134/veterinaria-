from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def producto_nuevo(request):
	if  request.method == 'POST':
		producto_form = ProductoForm(request.POST, request.FILES)
		if producto_form.is_valid():
			producto=producto_form.save()
			producto.save()
			return redirect('productos:listar_productos')
	else:
		producto_form=ProductoForm()


	return render(request, 'productos/producto_form.html',{'form':producto_form})

def gestionar_proformas(request):
	productos=Producto.objects.all()
	context={
			'productos':productos,
	}

	return render(request,'productos.html',context)

def gestionar_factura(request):
	productos=Producto.objects.all()
	context={
			'productos':productos,
	}

	return render(request,'productos.html',context)
def listar_productos(request):
	productos=Producto.objects.all()
	context={
			'productos':productos,
	}

	return render(request,'productos/producto_list.html',context)

def productoa_nuevo(request):
	return render(request, 'productos_agricolas.html',{}) 

def listar_agricolas(request):
	productos=Producto.objects.filter(tipo_producto__nombre="productos_agricolas")
	context={
			'productos':productos,
	}

	return render(request,'productos/producto_list.html',context)

def accesorios_nuevo(request):
	return render(request, 'accesorios.html',{}) 

def listar_accesorios(request):
	productos=Producto.objects.filter(tipo_producto__nombre="accesorios")
	context={
			'productos':productos,
	}

	return render(request,'productos/producto_list.html',context)

