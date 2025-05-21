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

#MODAL COMPONENT
def accordion_view(request):
    return render(request, 'documentation/pages/accordion.html')
