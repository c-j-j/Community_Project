from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from apps.jobs.models import Job


def index(request, template_name="jobs/index.html"):
    page_title = 'Jobs page'
    jobs = Job.objects.all()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def job_details(request, job_id, template_name="jobs/job_details.html"):
    job = get_object_or_404(Job, id=job_id)
    page_title = 'Job details for ' + job.title
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

