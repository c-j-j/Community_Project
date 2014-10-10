from django.template.defaultfilters import slugify
from django.test import TransactionTestCase

from apps.jobs.models import Job, Team


class JobsModelTests(TransactionTestCase):
    def setUp(self):
        self.some_team_name = "someTeam"
        self.team = Team.objects.create(name=self.some_team_name)
        self.team.save()

    def test_team_is_created_with_slug(self):
        persisted_team = Team.objects.get(pk=self.team.pk)
        self.assertEqual(persisted_team.slug, slugify(self.some_team_name))


    def test_job_can_be_created_and_refer_to_team(self):
        title = "someJobTitle"
        job = Job.objects.create(title=title, description="someDesc",
                                 skills="someSkills", team=self.team)
        job.save()

        found_job = Job.objects.get(title=title)

        self.assertEqual(found_job.description, job.description)
        self.assertEqual(found_job.team, job.team)

        # def test_job_are_sorted_in_most_recent_order(self):
        # jobA = Job.objects.create(title="someTitle", created_at=datetime.date(2014, 12, 1), description="someDesc",
        #                               skills="someSkills", team=self.team)
        #     jobB = Job.objects.create(title="someTitle", created_at=datetime.date(2014, 11, 1), description="someDesc",
        #                               skills="someSkills", team=self.team)
        #     jobC = Job.objects.create(title="someTitle", created_at=datetime.date(2014, 10, 1), description="someDesc",
        #                               skills="someSkills", team=self.team)
        #
        #     jobA.save()
        #     jobB.save()
        #     jobC.save()
        #
        #     jobs = Job.objects.all()
        #     self.assertEqual(jobs[0].id, jobA.id)
        #     self.assertEqual(jobs[1].id, jobB.id)
        #     self.assertEqual(jobs[2].id, jobC.id)



