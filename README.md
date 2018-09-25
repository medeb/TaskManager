# TaskManager
This is a simple task manager app where an user can track the record of the issues or tasks of their ongoing project. An user can
create a team & can assign task to the team members.<br/>
A demo link  can be found here : https://young-tor-21629.herokuapp.com/

# Important notes : Deploy app to Heroku 
Create a file without any extension named Procfile in the root directory and add :<br/>
  web: gunicorn TaskList.wsgi<br/>
  
Create runtime.txt and add your python version : python-3.6.6<br/>

Open setting.py and make these changes:<br/>

MIDDLEWARE_CLASSES = [<br/>
    'whitenoise.middleware.WhiteNoiseMiddleware',<br/>
]<br/>

STATIC_URL = '/static/'<br/>
STATICFILES_DIRS = [<br/>
        os.path.join(BASE_DIR, "static"),<br/>
    ]<br/>
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")<br/>

import dj_database_url<br/>
db_from_env = dj_database_url.config(conn_max_age=500)<br/>
DATABASES['default'].update(db_from_env)<br/>

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'<br/>



## Once you're done then use git and push it into heroku : 
git init <br/>
git add . <br/>
git commit -m "initial commit" <br/>
heroku create appname <br/>
git remote -v <br/>
heroku git:remote -a appname <br/>
git push heroku master <br/>
heroku python manage.py migrate <br/>
heroku python manage.py createsuperuser <br/>
heroku open 
