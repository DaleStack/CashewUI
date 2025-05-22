from django.urls import path
from .views import components_view, button_view, dropdown_view, modal_view, accordion_view, badge_view, card_view

urlpatterns = [
    path('components/', components_view, name='components_view'),
    path('components/button/', button_view, name='button_view'),
    path('components/dropdown/', dropdown_view, name='dropdown_view'),
    path('components/modal/', modal_view, name='modal_view'),
    path('components/accordion/', accordion_view, name='accordion_view'),
    path('components/badge/', badge_view, name='badge_view'),
    path('components/card/', card_view, name='card_view'),
]
