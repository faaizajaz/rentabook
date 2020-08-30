from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	kindle_email = forms.EmailField(required=True)

	class meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.is_active = False

		if commit:
			user.save()
		return user