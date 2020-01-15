from django.forms import ModelForm
from .models import Subdivision

class SubdivisionForm(ModelForm):
	class Meta:
		model = Subdivision
		fields = ['title', 'description', 'participants']
