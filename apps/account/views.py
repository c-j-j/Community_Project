from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render
from django.views import generic


class RegistrationForm(generic.FormView):
    form_class = UserCreationForm
    template_name = "registration/register.html"

    def get_success_url(self):
        return reverse('account:account_details', args=self.request.user.pk)

class UserAccount(generic.DetailView):
    model = User
    template_name = "registration/account_details.html"
