from django.shortcuts import render
from .models import OrderCatalog

# Create your views here.
def render_list(request):
	posts = OrderCatalog.objects.all()
	return render(request, 'datasheet/listview.html', {'posts': posts})