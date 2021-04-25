from django import forms

class regForm(forms.Form):
    First_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'placeholder':'First name'}))
    Email = forms.EmailField(max_length=50, widget = forms.TextInput(attrs = {'placeholder':'Email'}))
    Password = forms.CharField(max_length=20, widget = forms.PasswordInput(attrs = {'placeholder':'Password'}))
    Repassword = forms.CharField(max_length=20, widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password'}))
    terms = forms.BooleanField()

class loginForm(forms.Form):
    Username = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'placeholder':'Username'}))
    Password = forms.CharField(max_length=20, widget = forms.PasswordInput(attrs = {'placeholder':'Password'}))
