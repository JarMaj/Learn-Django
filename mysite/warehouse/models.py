from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Create your models here.

class Magazyn(models.Model):
    def __str__(self):
        return self.magazyn_text

    magazyn_text = models.CharField(max_length=50, verbose_name='Wpisz nazwe magazynu')

    class Meta:
        verbose_name_plural = 'Magazyny'
        verbose_name = 'Magazyny'


class Category(models.Model):
    def __str__(self):
        return self.category_text

    category_text = models.CharField(max_length=50, verbose_name='Wpisz nazwe kategorii', null=True, blank=True)

    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='user_id', verbose_name='Uzytkownik')

    class Meta:
        verbose_name_plural = 'Kategorie'
        verbose_name = 'Kategorie'


class Product(models.Model):
    def __str__(self):
        return self.product_text

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Wybierz kategorie')
    product_text = models.CharField(max_length=200, verbose_name='Wpisz nazwe produktu')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='Uzytkownik')
    magazyn = models.ForeignKey(Magazyn, on_delete=models.PROTECT, verbose_name='Wybierz magazyn', )
    dodaj_grafike = models.ImageField(verbose_name='Dodaj grafike')
    ilosc = models.IntegerField(default=1)
    jednostka = models.CharField(max_length=10, verbose_name="Jednostka", default='szt.')

    # def __add__(self, other):

    __original_ilosc = None

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.__original_ilosc = self.ilosc

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.ilosc != self.__original_ilosc:
            przed = self.__original_ilosc

            super(Product, self).save(force_insert, force_update, *args, **kwargs)
            self.__original_ilosc = self.ilosc
            # tu coś z przed trzeba zmienic
            po = self.ilosc

            user = self.user

            Product_Change_log.objects.create(
                ilosc_przed=przed,
                ilosc_po=po,
                log=self,
                change_date_time=datetime.datetime.now(),
                userp=user,

            )

    class Meta:
        verbose_name_plural = 'Produkty'
        verbose_name = 'Produkty'


class Product_Change_log(models.Model):
    def __str__(self):
        return 'log produktu ' + str(self.log)

    log = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='nazwa produktu', null=True, blank=True)
    change_date_time = models.DateTimeField(default=datetime.datetime.now)
    ilosc_przed = models.IntegerField(default=1, blank=True)
    ilosc_po = models.IntegerField(default=1, blank=True)

    userp = models.ForeignKey(User, verbose_name='Uzytkownik', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name_plural = 'Logi produktow'
        verbose_name = 'Logi produktow'

# stworzyc widok z boostrapem

# formularz za pomocą ktorego bedzie mozna wprowadzic towar na magazyn

# jak zbudować custom view w adminie customization admin
