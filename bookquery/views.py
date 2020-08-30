from django.shortcuts import render
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
#from 

# Create your views here.
@login_required
def SearchView(request, **kwargs):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.save()
			results = query.run_query_any_epub_or_mobi()
			for i in results:
				print(f"Title: {i['Title']} by {i['Author']} - ext: {i['Extension']}")
			
			# Now redirect to a different page (or use ajax) to display all 
			# the returned results, and allow user to choose.
			return render(request, 'bookquery/results.html', {'results': results})

	else:
		form = SearchForm()

	return render(request, 'bookquery/search.html', {'form': form})