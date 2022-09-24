from django import forms
from projects.models import project


class projectModerForm(forms.ModelForm):
    class Meta:
        model = project
        fields = '__all__'