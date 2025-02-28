# carapp/views.py
from django.shortcuts import render
from .forms import CarForm

def car_form(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model = form.cleaned_data['model']
            return render(request, 'carapp/result.html', {'manufacturer': manufacturer, 'model': model})
    else:
        form = CarForm()
    return render(request, 'carapp/car_form.html', {'form': form})
