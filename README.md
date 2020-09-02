# rentabook
![alt text](https://i.imgur.com/NFDN47M.png)
![alt text](https://i.imgur.com/RjI2fKn.png)
![alt text](https://i.imgur.com/7INfCFq.png)
![alt text](https://i.imgur.com/xZjBz1Npng)


## What is it?
A hastily written Django application that allows users to look up public domain and FOSS books on Libgen (libgen.is) and convert (if necessary) and download directly to a Kindle e-reader. It was designed to be easy to use for parents, grandparents, and other technology challenged family and friends, so functionality is kept deliberately lean.

## How was it made?
The website is built in Django 3.0 with a sprinkling of JQuery. A database (Postgres in this case) is required for the Django user auth system, and to keep track of queries in case I need to do any manual troubleshooting.

I also used some of the Libgen query code from: https://github.com/harrison-broadbent/libgen-api.

Calibre (https://calibre-ebook.com/) is used for file conversions.

Whitenoise is already configured to serve static files locally and in deployment.

## How to set up?
### Deploy on a VPS using Dokku
First set up a a basic VPS (I use Vultr, you can use [my affiliate link](https://www.vultr.com/?ref=7551767) or not) and install Dokku. Follow the instructions [here](http://dokku.viewdocs.io/dokku/getting-started/installation/) to get started.
#### On your server
* Install Dokku and create app on server
* Set up a DB
  * Install the Dokku postgres plugin from [here](https://github.com/dokku/dokku-postgres)
  * Create a new postgres db
  * link that with your app
* Set up persistent storage. The included `nginx.conf.sigil` will link `/media` in the app container to `/var/lib/dokku/storage/rentabook` on the host machine. You need to create this folder on the source machine, and add a `/converted` folder inside. The `dokku` user should have permissions to read and write.

#### On your local machine
* Clone the repo
* Update the `settings.py`
  * Add secret key
  * Configure SMTP
  * Add your domain to `ALLOWED_HOSTS`
  
#### Push to server
Follow the Dokku [docs](http://dokku.viewdocs.io/dokku/) to complete the deployment.

#### Create a Django admin superuser
You can do this by using the the `dokku run` command (`dokku run rentabook manage.py createsuperuser`) on your server

### Locally
The `settings.py` on this repo is set up so that you can deploy directly to a server running Dokku. However, with a little DJango knowledge, you should be able to get this up and running locally.
* Clone the repo
* Set up a venv
* Install dependencies from `requirements.txt`
* Update the `settings.py` for local development:
  * Add secret key
  * Configure SMTP for emails
  * Configure `MEDIA_ROOT` to store media files in a local folder (you can just use `/media`)
  * Configure `DATABASES` to use a local database (postgres will work out of the box, others you may need to tweak)
  * Add `127.0.0.1` (localhost) to `ALLOWED_HOSTS`
  
 ### On Heroku
 You may be able to get this running on Heroku, though you will definitely need to make some modifications. I have not tested this on Heroku.
 
 ## How to use?
 The registration route is `/iwantin` and the login route is `/gimme`. The rest is self-explanatory.
 
  
