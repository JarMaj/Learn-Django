from django.shortcuts import render

# Create your views here.
from .models import Product,Category
from django.views import generic
from django.utils import timezone

#Klasy do kategori
class IndexView(generic.ListView):
    template_name = 'warehouse/index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Category.objects.filter(
            pub_date_category__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Category
    template_name = 'warehouse/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Category.objects.filter(pub_date_category__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Category
    template_name = 'warehouse/results.html'


#Klasy do produktow


class IndexViewProduct(generic.ListView):
    template_name = 'warehouse/index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Product.objects.filter(
            pub_date_product__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailViewProduct(generic.DetailView):
    model = Product
    template_name = 'warehouse/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Product.objects.filter(pub_date_product__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Product
    template_name = 'warehouse/results.html'
