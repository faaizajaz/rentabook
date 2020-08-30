from django.shortcuts import render
from .forms import SearchForm
#from 

# Create your views here.
def SearchView(request, **kwargs):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.save()
			results = query.run_query_any()
			for i in results:
				print(f"Title: {i['Title']} by {i['Author']} - URL: {i['Mirror_1']}")
			
			# Now redirect to a different page (or use ajax) to display all 
			# the returned results, and allow user to choose.

	else:
		form = SearchForm()

	return render(request, 'bookquery/search.html', {'form': form})