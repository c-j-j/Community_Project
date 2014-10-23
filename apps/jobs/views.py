from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from apps.jobs.forms import CommentForm

from apps.jobs.models import Job, Team, JobComment


class IndexView(generic.ListView):
    template_name = "jobs/index.html"
    context_object_name = 'latest_jobs'
    someVar = "hello"

    def get_queryset(self):
        return Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['page_title'] = "Job Search"
        return context


class JobView(generic.DetailView):
    model = Job
    template_name = 'jobs/job_details.html'

    def get_context_data(self, **kwargs):
        context = super(JobView, self).get_context_data(**kwargs)
        context['page_title'] = "Job Details"
        return context


class TeamView(generic.DetailView):
    model = Team
    template_name = 'jobs/team_details.html'

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        context['page_title'] = "Team Details"
        context['form']=CommentForm()
        return context


class TeamList(generic.ListView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamList, self).get_context_data(**kwargs)
        context['page_title'] = "Team List"
        return context


class ProtectedView(generic.TemplateView):
    template_name = 'registration/login.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


class CreateTeamView(generic.CreateView):
    template_name = 'jobs/add_team.html'
    model = Team
    fields = ['name', 'description', 'location']

    def form_valid(self, form):
        form.instance.save()
        if self.request.user.is_authenticated():
            form.instance.users.add(self.request.user)
        return super(CreateTeamView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateTeamView, self).get_context_data(**kwargs)
        context['page_title'] = "Create Team"
        return context



class CreateJobView(generic.CreateView):
    template_name = 'jobs/add_job.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super(CreateJobView, self).get_context_data(**kwargs)
        context['page_title'] = "Create Job"
        return context


class JobComments(generic.View):
    def get(self, *args, **kwargs):
        jobComments = JobComment.objects.get(job__pk=kwargs['pk'])
        data = serializers.serialize("json", [jobComments,])
        return HttpResponse(data, content_type='application/json')
