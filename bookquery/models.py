from django.db import models
from libgenapi.libgen_search import LibgenSearch

class BookQuery(models.Model):
	title = models.CharField(max_length=1000, verbose_name='Title of book')
	author = models.CharField(max_length=1000, verbose_name='Author name')
	any_field = models.CharField(max_length=1000, verbose_name='Wildcard search')

	def __str__(self):
		return(f"Query for {self.title} by {self.author}")

	def run_query_title(self):
		search = LibgenSearch()
		results = search.search_title(self.title)
		return results

	def run_query_author(self):
		search = LibgenSearch()
		results = search.search_title(self.author)
		return results

	def run_query_any(self):
		search = LibgenSearch()
		results = search.search_title(self.any_field)
		return results