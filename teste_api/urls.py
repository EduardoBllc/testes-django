from django.urls import path
from teste_api.views import validador

urlpatterns = [
    path('validador', validador, name='validador'),
]