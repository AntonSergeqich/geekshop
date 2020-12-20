from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.url', namespace='products')),
    path('auth/', include('authapp.url', namespace='authapp')),
    path('basket/', include('basketapp.url', namespace='basket')),
    path('contact/', mainapp.contact, name='contact'),
    # path('admin/', admin.site.urls),
    path('admin/', include('adminapp.url', namespace='admin')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
