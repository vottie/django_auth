from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views

urlpatterns = [
#    url(r'^login/$','account.view.login.page',   name="user_login"),
#    url(r'^logout/$','account.view.logout.page', name="user_logout"),
#    url(r'^$', login_required(TemplateView.as_view(template_name='account/index.html')), name="index"),
    url(r'^profile/$', views.user_profile, name='user_profile'),
]

