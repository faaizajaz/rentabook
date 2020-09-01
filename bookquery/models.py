from django.db import models
from libgenapi.libgen_search import LibgenSearch
from django.contrib.auth.models import User

# Give the query model a results field that holds the dict of results (also includes urls)
# this is set in the search view

class BookQuery(models.Model):
	search_prompt = "Search for title, author, or both."
	# Search fields
	any_field = models.CharField(max_length=1000, verbose_name=search_prompt)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	# Fields populated after search


	def __str__(self):
		try:
			return(f"'{self.any_field}' by {self.user.username}")
		except AttributeError:
			return(f"'{self.any_field}' by unknown user")

	def run_query_title(self):
		search = LibgenSearch()
		results = search.search_title(self.title)
		return results

	def run_query_author(self):
		search = LibgenSearch()
		results = search.search_author(self.author)
		return results

	def run_query_any(self):
		search = LibgenSearch()
		results = search.search_any(self.any_field)
		return results

	def run_query_any_epub_or_mobi(self):
		search = LibgenSearch()
		results = search.search_any_epub_or_mobi(self.any_field)
		return results

	def get_download_api_url(self, book_id):
		from django.urls import reverse
		return reverse('download-book-api', args=book_id)
