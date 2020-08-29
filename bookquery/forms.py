from .models import BookQuery
from django.forms import ModelForm
from django.forms import CharField

class SearchForm(ModelForm):
	title = CharField(required=False)
	author = CharField(required=False)
	any_field = CharField(required=False)
	class Meta:
		model = BookQuery
		fields = ('title', 'author', 'any_field',)