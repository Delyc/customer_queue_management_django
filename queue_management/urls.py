from django.contrib import admin
from django.urls import path
from customers.views import get_waiting_time, index, register_customer, delete_customer, teller_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('register/<pk>', register_customer, name="register"),
    path("delete/<pk>", delete_customer, name="delete"),
    path("queue/<pk>",teller_view, name="teller-view" ),
    path("update/<pk>", get_waiting_time, name="update")
  
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
