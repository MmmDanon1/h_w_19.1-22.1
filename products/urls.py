from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product, name='product')
    # path('contact/', views.contact, name='contact'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('great_prod/', views.great_prod, name='great_prod'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)