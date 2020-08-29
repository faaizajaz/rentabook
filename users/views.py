from django.shortcuts import render
from .forms import UserRegistrationForm
from django.shortcuts import redirect

# Create your views here.
def RegisterUser(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})