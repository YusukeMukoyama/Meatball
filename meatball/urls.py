from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from accounts import views as accounts_views
from main import views as main_views
from accounts.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', accounts_views.root, name="root"),
    url(r'^signup$', accounts_views.signup, name="signup"),
    # url(r'^signup/', include('registration.backends.default.urls')),
    url(r'^regist_save$', accounts_views.regist_save, name='regist_save'),
    url(r'^login/$', login,
        {'template_name': 'accounts/login.html', 'authentication_form': LoginForm},
        name='login'),
    url(r'^logout$', accounts_views.logout_view, name='logout'),
    url(r'^index$', main_views.index, name="index"),
    url(r'^want/$', main_views.want, name="want"),
    url(r'^visited/$', main_views.visited, name="visited"),
    url(r'^add/$', main_views.add, name="add"),
    url(r'^detail/$', main_views.detail, name="detail"),
]
