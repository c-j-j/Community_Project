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


class CreateTeamView(generic.CreateView):
    template_name = 'jobs/add_team.html'
    model = Team
    fields = ['name', 'description', 'location']

    def form_valid(self, form):
        form.instance.save()
        if self.request.user.is_authenticated():
            form.instance.users.add(self.request.user)
        return super(CreateTeamView, self).form_valid(form)


class CreateJobView(generic.CreateView):
    template_name = 'jobs/add_job.html'
    model = Job
