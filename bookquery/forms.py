from .models import BookQuery
from django.forms import ModelForm


class SearchForm(ModelForm):
	#title = CharField(required=False)
	#author = CharField(required=False)
	#any_field = CharField(required=False)
	#email = CharField(required=True, label='Kindle email address')
	class Meta:
		model = BookQuery
		exclude = ['user']