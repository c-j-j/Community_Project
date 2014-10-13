from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import generic


class RegistrationForm(generic.FormView):
    template_name = "registration/register.html"

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        form = UserCreationForm(post_data)
        if form.is_valid():
            form.save()
            username = post_data.get('username', '')
            password = post_data.get('password1', '')
            new_user = authenticate(username=username, password=password)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = reverse('account:account_details')
                return HttpResponseRedirect(url)

        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))



class UserAccount(generic.View):
    template_name = "registration/account_details.html"
    def get(self, instance):
        user = self.request.user
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(self.request))

