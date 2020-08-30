from django.db import models
from libgenapi.libgen_search import LibgenSearch

# Give the query model a results field that holds the dict of results (also includes urls)
# this is set in the search view

class BookQuery(models.Model):
	search_prompt = "Enter as many keywords about the book as possible"
	# Search fields
	title = models.CharField(max_length=1000, verbose_name='Title of book')
	author = models.CharField(max_length=1000, verbose_name='Author name')
	any_field = models.CharField(max_length=1000, verbose_name=search_prompt)

	# Fields populated after search


	def __str__(self):
		return(f"Query for {self.title} by {self.author}")

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
