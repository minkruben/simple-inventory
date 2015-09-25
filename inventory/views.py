from django.shortcuts import render
from django.http import Http404

from inventory.models import Item
from django.http import HttpResponse

# Create your views here.

def index(request):
	#return HttpResponse('<p> In index view </p>')
	items = Item.objects.exclude(amount=0)
	return render(request, 'inventory/index.html', {
			'items':items,
		})


def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This Item does not exist')
	return render(request, 'inventory/item_detail.html', {
			'item': item,
		})
	#return HttpResponse('<p> In index_detail view with id {0} </p>'.format(id))