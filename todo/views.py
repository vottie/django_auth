from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        # reffer django-document.
        # Built-in class-based generic views > Dynamic.filtering
        # print(self.request.user)
        return Todo.objects.filter(user_id = self.request.user.id)
