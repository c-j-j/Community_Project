from django.core.urlresolvers import reverse
from django.test import TransactionTestCase

from apps.jobs.models import Job, Team


class IndexViewTests(TransactionTestCase):
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
        self.assertTemplateUsed(response,"jobs/index.html")

    def test_job_details(self):
        some_team = Team.objects.create(name="someTeamName", description="someTeamDescription", slug="someTeamSlug")
        some_job = Job.objects.create(title='someJobTitle', description="someJobDescription", team=some_team)

        response = self.client.get(reverse('jobs:job_detail', args=[str(some_job.pk)]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['job'].pk, some_job.pk)
        self.assertEqual(response.context['job'].team, some_team)
        self.assertTemplateUsed(response,"jobs/job_details.html")


    def test_team_details(self):
        some_team = Team.objects.create(name="someTeamName", description="someTeamDescription", slug="someTeamSlug")

        response = self.client.get(reverse('jobs:team_detail', args=[some_team.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['team'].pk, some_team.pk)
        self.assertTemplateUsed(response,"jobs/team_details.html")
