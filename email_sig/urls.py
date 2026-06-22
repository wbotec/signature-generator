from django.urls import path, include

urlpatterns = [
    path('', include('signature_app.urls')),
]
