# carapp/forms.py
from django import forms

CAR_MANUFACTURERS = [
    ('toyota', 'Toyota'),
    ('ford', 'Ford'),
    ('honda', 'Honda'),
    ('chevrolet', 'Chevrolet'),
]

class CarForm(forms.Form):
    manufacturer = forms.ChoiceField(choices=CAR_MANUFACTURERS, label="Select Manufacturer")
    model = forms.CharField(max_length=100, label="Car Model")
