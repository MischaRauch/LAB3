from django.shortcuts import get_object_or_404, render

from .models import Pizza


def index(request):
    pizza_list = Pizza.objects.order_by('-id')[:5]
    context = {'pizza_list': pizza_list}
    return render(request, 'menu/index.html', context)

def detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    return render(request, 'menu/detail.html', {'pizza': pizza})
