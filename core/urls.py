from django.urls import path

from core.views import index, contact, produto

urlpatterns = [
    path('', index, name='index'),
    path('contatos', contact, name='contact'),
    path('produto/<int:pk>', produto, name='produto'), 
]
