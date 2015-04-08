from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from client.models import User



class FileUploadForm(forms.Form):
    file_field = forms.FileField(label="", required=True)

class RegistrationForm(ModelForm):
    username        = forms.CharField(label=(u'User Name'))
    email           = forms.EmailField(label=(u'Email Address'))
    password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    

    class Meta:
        model = User
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
        	User.objects.get(username=username)
        except User.DoesNotExist:
                return username
        raise forms.ValidationError("That username is already taken, please select another.")