from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from website.models import Customer

#registration form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=30, required=False, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
           
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        
#add customer form
class AddCustomerForm(forms.ModelForm):
    First_name = forms.CharField(max_length=50, label="First Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    Last_name = forms.CharField(max_length=50, label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    Email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    Phone = forms.CharField(max_length=15, label="Phone", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    Address = forms.CharField(max_length=100, label="Address", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    City = forms.CharField(max_length=50, label="City", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    State = forms.CharField(max_length=50, label="State", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    Zip_code = forms.CharField(max_length=10, label="Zip Code", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}))
    
    class Meta:
        model = Customer
        fields = ['First_name', 'Last_name', 'Email', 'Phone', 'Address', 'City', 'State', 'Zip_code']