from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField

class UserRegistrationForm(UserCreationForm):
	email = EmailField(required=True, label='Kindle email address', help_text='This needs to be your send-to-Kindle address. Check your Amazon settings if you\'re not sure.')
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.is_active = False

		if commit:
			user.save()
		return user