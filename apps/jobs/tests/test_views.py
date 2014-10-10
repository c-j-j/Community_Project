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
        some_team = Team.objects.create(name="someTeamName", description="someTeamDescription", slug="someTeamSlug")
        some_job = Job.objects.create(title='someJobTitle', description="someJobDescription", team=some_team)
        response = self.client.get(reverse('jobs:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_jobs'], [('<Job: %s>' % some_job.title)])
        self.assertTemplateUsed("jobs/index.html")


    def test_job_details(self):
        some_team = Team.objects.create(name="someTeamName", description="someTeamDescription", slug="someTeamSlug")
        some_job = Job.objects.create(title='someJobTitle', description="someJobDescription", team=some_team)

        response = self.client.get(reverse('jobs:detail', args=[some_job.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['job'].pk, some_job.pk)
        self.assertEqual(response.context['job'].team, some_team)


    def test_team_details(self):
        some_team = Team.objects.create(name="someTeamName", description="someTeamDescription", slug="someTeamSlug")

        response = self.client.get(reverse('jobs:team', args=[some_team.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['team'].pk, some_team.pk)
