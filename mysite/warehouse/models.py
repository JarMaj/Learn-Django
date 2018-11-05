from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='user_id', verbose_name='Uzytkownik')
    magazyn = models.ForeignKey(Magazyn, on_delete=models.PROTECT, verbose_name='Wybierz magazyn', )
    dodaj_grafike = models.ImageField(verbose_name='Dodaj grafike')
    ilosc = models.IntegerField(default=1)
    jednostka = models.CharField(max_length=10, verbose_name="Jednostka", default='szt.')

    # def __add__(self, other):

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # kod przed save



        super(Product, self).save(*args, **kwargs)

        if hasattr(self, 'force_sync'):
            force_sync = self.force_sync
        else:
            force_sync = True

    class Meta:
        verbose_name_plural = 'Produkty'
        verbose_name = 'Produkty'


class Product_Change_log(models.Model):
    # def __str__(self):
    # return self.log

    # product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='nazwa produktu')
    log = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='', null=True, blank=True)
    change_date_time = models.DateTimeField(default=timezone.now())
    ilosc_przed = models.IntegerField(default=1, blank=True)
    ilosc_po = models.IntegerField(default=1, blank=True)

    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Uzytkownik')
    class Meta:
        verbose_name_plural = 'Logi'
        verbose_name = 'Logi'
