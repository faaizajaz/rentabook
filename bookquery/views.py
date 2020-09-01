from django.shortcuts import render
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
import urllib.request
from bs4 import BeautifulSoup
import subprocess
from django.core.mail import EmailMessage
from rentabook import settings
import os


# Create your views here.
@login_required
def SearchView(request, **kwargs):
	print(f"Request made by {request.user.username}")
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.save(commit=False)
			results = query.run_query_any_epub_or_mobi()
			# Now redirect to a different page (or use ajax) to display all 
			# the returned results, and allow user to choose.
			request.session['search_results'] = results
			query.user = request.user
			query.save()
			if len(results) != 0:
				return render(request, 'bookquery/results.html', {'results': results})
			else: 
				return render(request, 'bookquery/noresults.html')

	else:
		form = SearchForm()

	return render(request, 'bookquery/search.html', {'form': form})


class DownloadView(APIView):
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request, book_id=None):
		try:
			for book in request.session['search_results']:
				if book["ID"] == book_id:
					match_book = book
					request.session['match_book'] = match_book

			print(f"{request.user.username} is searching for {match_book['Title']}")

			mirror_1_url = match_book['Mirror_1']
			mirror_2_url = match_book['Mirror_2']

			with urllib.request.urlopen(mirror_1_url) as download_page:
				download_page_html = download_page.read()

			soup = BeautifulSoup(download_page_html, 'html.parser')

			download_link = soup.h2.a.get('href')

			print("downloading")

			file_title = f"{match_book['Title']}.{match_book['Extension']}"
			file_mobi_title = f"{match_book['Title']}.mobi"
			converted_path = os.path.join(settings.MEDIA_ROOT, f"converted/{file_mobi_title}")
			#converted_path = f"media/converted/{file_mobi_title}"
			

			#urllib.request.urlretrieve(download_link, f"media/{file_title}")
			urllib.request.urlretrieve(download_link, os.path.join(settings.MEDIA_ROOT, file_title))

			print("downloaded book!")

			# Now check if it is epub, and convert if sorted
			converted = False
			if match_book['Extension'] == "epub":
				print("it is epub so i'll try to convert")
				try:
					print("Converting...")
					#subprocess.call(["ebook-convert", f"media/{file_title}", converted_path])
					subprocess.call(["ebook-convert", os.path.join(settings.MEDIA_ROOT, file_title), converted_path])
					converted = True
					attachment_path = converted_path
					print("Successfully converted!")

					
				except Exception as e:
					print(e)
			else:
				#attachment_path = f"media/{file_title}"
				attachment_path = os.path.join(settings.MEDIA_ROOT, file_title)

			# Now email it
			subject = f"Emailing: {file_mobi_title}"
			body = ""
			from_email = settings.EMAIL_HOST_USER
			to = (request.user.email,)

			email = EmailMessage(subject=subject, body=body, from_email=from_email, to=to)
			email.attach_file(attachment_path)
			print(f"Attached {attachment_path}")
			email.send()
			print(f"sent email to {request.user.email}")


			#Some data to return to your jquery ajax call
			data = {
				"Title": match_book['Title'],
				"Successful": True,
				"Converted": converted
			}

			return Response(data, status=status.HTTP_200_OK)
			#download the file
		except:
			data = {
				"Successful": False
			}
			return Response(data, status=status.HTTP_400_BAD_REQUEST)
