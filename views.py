from django.http import HttpResponse
from django.shortcuts import render

from models import order
from .forms import orderForm


def add_order(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('order added to database')
        else:
            form = orderForm()
        return render(request, 'add_order.html', {'order_form': form})
def order_list(request):
 return render(request,'order_list.html',{
     'order' : order.objects.all()
 })


