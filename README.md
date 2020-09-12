# rentabook
![alt text](https://i.imgur.com/NFDN47M.png)
![alt text](https://i.imgur.com/RjI2fKn.png)
![alt text](https://i.imgur.com/7INfCFq.png)
![alt text](https://i.imgur.com/TY2QA1x.png)


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
##### Install Dokku
SSH into your server and do:
`$ wget https://raw.githubusercontent.com/dokku/dokku/v0.21.4/bootstrap.sh`
`$ sudo DOKKU_TAG=v0.21.4 bash bootstrap.sh`

In a browser, go to the ip address of your server and paste your SSH public key into the box. Check the Dokku docs for more details. You can also ad your public key manually by uploading to the server, and then add the keys to dokku by doing:
`$ sudo dokku ssh-keys:add <name_for_key> /path/to/key`

Check to see that your key was added by doing:
`$ dokku ssh-keys:list`

Then, allow the Dokku user to log in via SSH (you need to do this if you have disabled password based login and added an `AllowUser` setting in your `sshd_config`

##### Create a Dokku app and Postgres database
`$ doku apps:create <your_app>`

Install the Postgres plugin
`$ sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git`

Create a DB and link to your app
`dokku postgres:create <db_name>`
`dokku postgres:link <db_name> <your_app>`

##### Configure your domains and add git repo
Check the dokku docs for more details on domains. For this purpose, I assume you are deploying to `subdomain.domain.tld`
`$ dokku domains:add <your_app> subdomain.domain.tld`

Add your repo from your local development machine 
`> git remote add dokku dokku@<host>:<your_app>`

Make sure to add your domain to `ALLOWED_HOSTS` in `settings.py`

##### Set up persistent storage
Dokku's default mount point inside the ontainer is `/storage`. You should have no reason to change this, but if you do, refer to the Dokku docs.

On your server, create a folder for your app's storage:
`$ mkdir -p /var/lib/dokku/data/storage/<your_app>`

Then, set permissions so Dokku and your container have access (32767 is the default container group here):
`$ sudo chown -R dokku:dokku /var/lib/dokku/data/storage/<your_app>`
`$ sudo chown -R 32767:32767 /var/lib/dokku/data/storage/<your_app>`

Then, mount your storage to the `/storage` folder in your container:
`$ dokku storage: mount <appname> /var/lib/dokku/data/storage/<your_app>:/storage`

Check that it is mounted correctly, then restart
`$ dokku storage:list <your_app>`
`$ dokku ps:rebuild <your_app>`

Now, the storage folder will remain mounted unless you destroy and redeploy your server

##### Configure Nginx to serve files from the mounted storage
If you use the step above to configure your persistent storage and use the default static files and media files in the included `settings.py`, then this will already be done for you through the `ngingx.conf.sigil` so you do not need to do anything else.

#### On your local machine
* Clone this repo
* Update the `settings.py`
  * Add secret key
  * Configure SMTP
  * Add your domain to `ALLOWED_HOSTS`
  
#### Push to server
Follow the Dokku [docs](http://dokku.viewdocs.io/dokku/) to complete the deployment.

You should just be able to do (from the root of the cloned repo on your local machine):
`> git push dokku master:master`

This assumes that you are deploying the `master` branch of the cloned repo (there is only one branch, so this will be default unless you add a branch.

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
 
  
