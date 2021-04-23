from django.contrib.auth.models import User
from django import forms
from .models import Booking,Driver


FROM_LOCATION=(
    ('Kuniyamuthur','Kuniyamuthur'),
    ('Ukkadam','Ukkadam'),
    ('Gandhipuram','Gandhipuram'),
    ('Sundharapuram','Sundharapuram'),
)

TO_LOCATION=(
    ('Kuniyamuthur','Kuniyamuthur'),
    ('Ukkadam','Ukkadam'),
    ('Gandhipuram','Gandhipuram'),
    ('Sundharapuram','Sundharapuram'),
)

LOCATION=(
    ('Kuniyamuthur','Kuniyamuthur'),
    ('Ukkadam','Ukkadam'),
    ('Gandhipuram','Gandhipuram'),
    ('Sundharapuram','Sundharapuram'),
)


class BookingForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Your name',

    }))
    email=forms.EmailField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Email address',
    'type':'email',

    }))
    phone=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control ',
    'placeholder':'Phone Number',

    }))
    passenger=forms.IntegerField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Passenger Count',
    'type':'number',

    }))

    StartLocation = forms.ChoiceField(choices=FROM_LOCATION,required=True)
    ToLocation = forms.ChoiceField(choices=TO_LOCATION,required=True)

    class Meta:
        model=Booking
        fields=['name','email','phone','StartLocation','ToLocation','passenger']

class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Your name',

    }))
    email=forms.EmailField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Email address',
    'type':'email',

    }))

    password=forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder':'Enter the password',
    }))

    class Meta:
        model=User
        fields=('username','email','password')


class Driverform(forms.ModelForm):
    # name=forms.CharField(widget=forms.TextInput(attrs={
    # 'class':'form-control',
    # 'placeholder':'Your name',
    #
    # }))

    phone=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control ',
    'placeholder':'Phone Number'

    }))

    lic_no=forms.IntegerField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'License Number',
    'type':'number',

    }))
    vehicle_no=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control ',
    'placeholder':'Vehicle No',

    }))

    Location = forms.ChoiceField(choices=LOCATION,required=True)




    class Meta:
        model=Driver
        fields=['phone','lic_no','vehicle_no','Location']
