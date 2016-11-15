from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth.views import logout

from testproject.views import login


urlpatterns = [

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, {'next_page': '/'}, name='logout'),
    url(r'^', include('fpr.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
