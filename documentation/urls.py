from django.urls import path
from .views import components_view, button_view

urlpatterns = [
    path('components/', components_view, name='components_view'),
    path('components/buttons/', button_view, name='button_view'),
]
