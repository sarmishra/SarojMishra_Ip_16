from django.conf.urls import url
from .views import home,dashboard,signup
from django.contrib.auth.views import login as auth_login, logout as auth_logout

urlpatterns = [
    url(r'^$', auth_login,{'template_name': 'login/login.html'},name='login'),
	url(r'logout/$', auth_logout, {'next_page': '/'}, name='logout'),
    url(r'dashboard/$', dashboard,name='dashboard' ),

    url(r'signup/$', signup,name='signup' ),

]
