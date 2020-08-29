from django.shortcuts import render
from .forms import SearchForm

# Create your views here.
def SearchView(request, **kwargs):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			print("something")

	else:
		form = SearchForm()

	return render(request, 'bookquery/search.html', {'form': form})