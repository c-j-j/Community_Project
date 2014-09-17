from django.core.urlresolvers import reverse
from django.test import TestCase
from apps.jobs.models import Job, Team


class IndexViewTests(TestCase):
    def test_index_view_no_jobs(self):
        response = self.client.get(reverse('jobs:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No jobs available")
        self.assertQuerysetEqual(response.context['latest_jobs'], [])

    def test_index_view_with_job(self):
        some_team = Team.objects.create(name="someTeamName", description="someTeamDescription")
        some_job = Job.objects.create(title='someJobTitle', description="someJobDescription", team=some_team)
        response = self.client.get(reverse('jobs:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_jobs'], [('<Job: %s>' % some_job.title)])
        self.assertTemplateUsed("jobs/index.html")
