"""
This is where the urls.py will redirect to.
it redirects to one of the functions below.
Noted that an "request" argument must be presented as the first argument, to handle HTTP stuff (I guess),
except for Generic view (which I have no idea on)
"""
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Supply,Order,Include


#temp index page
def index(request):
    # this is the simplest form, returning a Response containing the message only.
	return HttpResponse("index page")

#for generic detail view	
#use the primary key in the url
#detail of a supply
class DetailView(generic.DetailView):
	model = Supply #where to search for primary key
	template_name = "system/detail.html"
	
#for generic lsit view
#use def get_queryset and return a list
class DispatchView(generic.ListView):
	context_object_name = 'orderList'
	#equal to pass a list
	#{orderList: queryset}
	template_name = "system/dispatch.html"
	def get_queryset(self):
		return Order.objects.filter(status="Queued for dispatch").order_by('orderedDatetime')
		
#if not use generic view, use render to call html
#cat is the category name
def displayByCategory(request,cat):
	supply = Supply.objects.filter(category=cat)
	list = {'list':supply}
	return render(request,"system/displayByCategory.html",list)
	
#detail of specific order
def orderView(request,orderID):
    # preforming query for cretain objects.
	order = Order.objects.get(pk=orderID)
	supply = Include.objects.filter(order_id=orderID)
	list = {'order':order,'supplyList':supply}
	return render(request,"system/order.html",list)

def createOrder(request):
    # redirect to createOrder.html and renders it. (noted that the .html files are under .templates/system/)
    # but in django templates is default and it's omitted. don't add templates in from of directory.
	return render(request, "system/createOrder.html")

def createOrder2(request):
	query = request.GET.get('query')
	try:
		query = int(query)
	except ValueError:
		query = None
	if query:
		clinic = request.GET.get('clinicID')
		dateTime = timezone.now()
		priority = request.GET.get('priority')
		items = request.GET.get('items')
		weight = request.GET.get('weight')
		resultOrder = Order.create(priority=priority, items=items, ODatetime=dateTime, cid=clinic, weight=weight)
		resultOrder.save()
		result = "success"
	else:
		result = None
	context = RequestContext(request)
	return render_to_response("system/createOrder.html", {"result": result, }, context_instance=context)
