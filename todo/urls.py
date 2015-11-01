from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view(
               template_name='todo/index.html')), name="index"),
]
