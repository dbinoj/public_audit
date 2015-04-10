
from django import forms
class  login_userForm(forms.Form):
    username        = forms.CharField(label=(u'UserName'))
    password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        