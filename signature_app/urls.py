from django.urls import path
from . import views

app_name = 'signature_app'

urlpatterns = [
    path('', views.generator, name='generator'),
]
