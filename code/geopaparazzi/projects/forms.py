from django.forms import ModelForm, Textarea, TextInput, SelectMultiple
from .models import Subdivision
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class OwnSelectWidget(forms.SelectMultiple):
    class Media:
        css = {'all': ( "projects/my_sripts.css", )}
        js = ('projects/my_sripts.js',)


class SubdivisionForm(ModelForm):
    #Здесь можно как в forms.Form переопределять поля модели
    participants = forms.ModelMultipleChoiceField(
        label='Участники:', 
        queryset=User.objects.all(), 
        widget = OwnSelectWidget(attrs={
            'class': "form-control",
            'required': "false",
            'autocomplete': "off"}))

    class Meta:
        model = Subdivision
        fields = ['title', 'description', 'participants']
        widgets = {
            'title': TextInput(attrs={
                'class' : "form-control",
                'required': "true",
                'autocomplete':"off",
                }),
            'description': Textarea(attrs={
                'cols': 10,
                'rows': 5,
                'class' : "form-control",
                }),
        }

        

