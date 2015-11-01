from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
 
# Create your views here.
#def index():
#    return HttpResponseRedirect()

@login_required
def user_profile(request):
    context = RequestContext(request,
                             {'user': request.user})
    return render_to_response('account/user_profile.html',
                              context_instance=context)
