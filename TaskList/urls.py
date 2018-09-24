from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('TaskAssignment.urls')),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/accounts/login/'},name='logout'),
]


# (r'^login/$',
#     'django.contrib.auth.views.login', {'template_name': 'login.html'}
# )