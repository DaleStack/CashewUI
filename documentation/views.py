from django.shortcuts import render

# Create your views here.
def components_view(request):
    return render(request, 'documentation/components.html')

#ACTIONS

#BUTTON COMPONENT
def button_view(request):
    return render(request, 'documentation/pages/button.html')

#DROPDOWN COMPONENT
def dropdown_view(request):
    return render(request, 'documentation/pages/dropdown.html')

#MODAL COMPONENT
def modal_view(request):
    return render(request, 'documentation/pages/modal.html')

#DATA DISPLAY

#ACCORDION COMPONENT
def accordion_view(request):
    return render(request, 'documentation/pages/accordion.html')

#BADGE COMPONENT
def badge_view(request):
    return render(request, 'documentation/pages/badge.html')

#CARD COMPONENT
def card_view(request):
    return render(request, 'documentation/pages/card.html')

#ALERT COMPONENT
def alert_view(request):
    return render(request, 'documentation/pages/alert.html')

#TOOLTIP COMPONENT
def tooltip_view(request):
    return render(request, 'documentation/pages/tooltip.html')

#SELECT COMPONENT
def select_view(request):
    return render(request, 'documentation/pages/select.html')