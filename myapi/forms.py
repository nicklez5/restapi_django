from django import forms
from myapi.models import CustomUser,Machine,Timecard,Job
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'name',
            'is_admin'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control','size':'40'}),
            'is_admin': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class UpdateCustomUserForm(UserChangeForm):
    username = forms.CharField()
    name = forms.CharField()

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username ')

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'code',
            'description',
            'hourly_rate',
            'maxhoursperday'
        ]

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'machine_code',
            'description',
            'hourly_rent',
            'maxhoursperday'
        ]

class TimecardForm(forms.ModelForm):
    class Meta:
        model = Timecard
        fields = [
            'sitecode',
            'contractor_name',
            'total_hours',
            'total_amount'
        ]
        exclude = ('status')

class UpdateTimecard(forms.ModelForm):
    sitecode = forms.CharField()
    contractor_name = forms.CharField()
    total_hours = forms.IntegerField()
    total_amount = forms.FloatField()

class UpdateMachine(forms.ModelForm):
    machine_code = forms.CharField()
    description = forms.CharField()
    hourly_rent = forms.FloatField()
    maxhoursperday = forms.IntegerField()

class UpdateJob(forms.ModelForm):
    code = forms.CharField()
    description = forms.CharField()
    hourly_rate = forms.FloatField()
    maxhoursperday = forms.IntegerField()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'name'
        ]
