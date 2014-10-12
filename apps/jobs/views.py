from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from apps.jobs.models import Job, Team


class IndexView(generic.ListView):
    template_name = "jobs/index.html"
    context_object_name = 'latest_jobs'

    def get_queryset(self):
        return Job.objects.all()


class JobView(generic.DetailView):
    model = Job
    template_name = 'jobs/job_details.html'


class TeamView(generic.DetailView):
    model = Team
    template_name = 'jobs/team_details.html'


class TeamList(generic.ListView):
    model = Team


class ProtectedView(generic.TemplateView):
    template_name = 'registration/login.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


class CreateTeamView(generic.CreateView, ProtectedView):
    template_name = 'jobs/add_team.html'
    model = Team


    # def get_context_data(self, **kwargs):
    #     context = super(CreateTeamView, self).get_context_data(**kwargs)
    #     context['new_addition'] = 'True'
    #     return context


class CreateJobView(generic.CreateView):
    template_name = 'jobs/add_job.html'
    model = Job
