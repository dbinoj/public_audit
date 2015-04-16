from django import forms
class  LoginUserForm(forms.Form):
    username = forms.CharField(label=(u'UserName'),widget=forms.TextInput(attrs={'class': "form-control",'autofocus':'autofocus','placeholder':'Username','required':'required'}))
    password = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(attrs={'class': "form-control",'placeholder':'Password','required':'required'}))
