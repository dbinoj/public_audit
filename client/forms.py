from django import forms


class FileUploadForm(forms.Form):
    file_field = forms.FileField()
