from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *
import requests

# Create your views here.
def main(request):
	return render(request, 'datasheet/main.html', {})

def render_list(request):
	posts = OrderCatalog.objects.filter(status="New")
	form = UploadConfirmForm()
	return render(request, 'datasheet/listview.html', {'posts': posts, 'form': form})

def upload(request):
	lists = OrderCatalog.objects.filter(status="Done")
	data = {}
	for row in lists:
		data['session'] = request.POST.get("cookie","")
		data['code'] = row.code
		data['longdesc'] = row.long_desc
		data['shortdesc'] = row.short_desc
		data['ordercate'] = row.order_type.order_cate
		data['ordertype'] = row.order_type.code
		data['activitytype'] = row.activity_type
		data['part'] = ""
		data['index'] = "N"

		r = requests.get("http://127.0.0.1:1880/upload", params=data)
		row.status = r.text
		row.save()
	return HttpResponseRedirect(reverse('main'))