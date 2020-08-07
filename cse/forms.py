from django import forms
from .models import ImagesUpload

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagesUpload
        fields = ['subject', 'semester', 'description', 'image']