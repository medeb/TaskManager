
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required, permission_required

app_name='tasks'

urlpatterns = [
    url(r'^$',login_required(views.HomePageView.as_view()),name="home_page"),
    url(r'^add/task$',login_required(views.CreateTaskView.as_view()),name="createTask"),
    url(r'^task/(?P<pk>[0-9]+)/$',login_required(views.DetailTaskView),name="detailTask"),
    url(r'^add/team$',login_required(views.CreateTeamView.as_view()),name="createTeam"),
    url(r'^team/(?P<pk>[0-9]+)/members/$',login_required(views.AddTeamMemView.as_view()),name="team_members"),
    url(r'^team/(?P<id_team>[0-9]+)/tasks$',login_required(views.CardDetialView),name="taskList"),
]
