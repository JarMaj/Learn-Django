# Create your views here.
import datetime


from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


from .models import Product


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class ProductViewInTable(TemplateView):
    model = Product
    template_name = '/home/jarek/PycharmProjects/Jarektesty/mysite/templates/mysite/test.html'


    def extented_view(request):


        #return HttpResponse(output, template)
        return render(request, ProductViewInTable.template_name, {})

    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductViewInTable, self).get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()

        return context


    def search(request):
        terms = request.GET.get('terms', None)
        term_list = terms.split(' ')

        products = Product.objects.all()

        q = Q(content__icontains=term_list[0]) | Q(title__icontains=term_list[0])
        for term in term_list[1:]:
            q.add((Q(content__icontains=term) | Q(title__icontains=term)), q.connector)

        products = products.filter(q)

        return render_to_response('/home/jarek/PycharmProjects/Jarektesty/mysite/templates/mysite/test.html',
                                products)












