"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from warehouse.views import current_datetime

from warehouse.views import ProductViewInTable

"""
class CustomAdminSite(admin.AdminSite):
    @never_cache
    def index(self, request, extra_context=None):
        ret = super(CustomAdminSite, self).index(request, extra_context)
        # SEU CODIGO AQUI
        return ret

#admin.site = CustomAdminSite()
#admin.autodiscover()


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        from django.urls import path

        urls = super().get_urls()
        urls += [
            path('widok/', self.admin_view(views.py))
        ]
        return urls
"""


admin.autodiscover()
urlpatterns = [

    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('warehouse/', include('warehouse.urls')),
    path('nasz_widok/', current_datetime),
    path('nowy_widok/', ProductViewInTable.as_view()),






]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
