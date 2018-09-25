# TaskManager
This is a simple task manager app where an user can track the record of the issues or tasks of their ongoing project. An user can
create a team & can assign task to the team members.
A demo link  can be found here : https://young-tor-21629.herokuapp.com/

# Important notes : Deploy app to Heroku 
Create a file without any extension named Procfile in the root directory and add :
  web: gunicorn TaskList.wsgi
  
Create runtime.txt and add your python version : python-3.6.6

Open setting.py and make these changes:

MIDDLEWARE_CLASSES = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



## Once you're done then use git and push it into heroku : 
git init
git add .
git commit -m "initial commit"
heroku create appname
git remote -v
heroku git:remote -a appname
git push heroku master
heroku python manage.py migrate
heroku python manage.py createsuperuser
heroku open
