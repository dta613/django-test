from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.views.generic.list import ListView
import json
from django import forms
from dashboard.forms import Patient_form
from dashboard.models import Patient
from django.views.generic.edit import FormView




# Create your views here.



from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from TEST.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Create your views here.

def IndexView(request):
    return HttpResponse(render(request, "index.html"))

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        render(request, "login_success.html")
    else:
        #Return an 'invalid' login error message
        render(request, "login_failure.html")

#No longer used
# class Patient_list(ListView):
#     model = Patient
#

class IndexView(generic.ListView):
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'Patient'
    def get_queryset(self):
        """Return the last five visit."""
        return Patient.objects.order_by('initial_visit')[:5]

class MyFormView(FormView):
    form_class = Patient_form
    template_name = 'dashboard/form.html'
    success_url = 'dashboard'

    def get_context_data(self, **kwargs):
        #This is you GET
        return super(MyFormView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        #This is after the post, when the form is valid
        return super(MyFormView, self).form_valid(form)

    def form_invalid(self, form):
        #This is after the post, when the form is invalid
        return super(MyFormView, self).form_invalid(form)

    def get_name(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':

            # create a form instance and populate it with data from the request:
            form = Patient_form(request.POST)
            # check whether it's valid:

            if form.is_valid():
                # process the data in form.cleaned_data as required
                post = request.POST
                Patient_form = form.save()
                # redirect to a new URL:
            else:
                print("This form is not working well")
        # if a GET (or any other method) we'll create a blank form
        else:
            form = Patient_form
            return render(request, 'form.html',)

#class ArticleListView(ListView):

#    model = Article

#    def get_context_data(self, **kwargs):
#        context = super(ArticleListView, self).get_context_data(**kwargs)
#        context['now'] = timezone.now()
#        return context


#def get_name(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#        form = NameForm(request.POST)
#        # check whether it's valid:
#        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
#            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = NameForm()

#    return render(request, 'name.html', {'form': form})
