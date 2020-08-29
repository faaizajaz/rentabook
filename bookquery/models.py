from django.db import models

class BookQuery(models.Model):
	title = models.CharField(max_length=1000, verbose_name='Title of book')
	author = models.CharField(max_length=1000, verbose_name='Author name')

	def __str__(self):
		return(f"Query for {self.title} by {self.author}")