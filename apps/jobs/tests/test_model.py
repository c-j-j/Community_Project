import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from apps.jobs.models import Job, Team


class JobsModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="someTeam")

    def test_job_can_be_created_and_refer_to_team(self):
        title = "someJobTitle"
        job = Job.objects.create(title=title, description="someDesc",
                                 skills="someSkills", team=self.team)

        found_job = Job.objects.get(title=title)

        self.assertEqual(found_job.description, job.description)
        self.assertEqual(found_job.team, job.team)

    # def test_job_are_sorted_in_most_recent_order(self):
    #     jobA = Job.objects.create(title="someTitle", created_at=datetime.date(2014, 12, 1), description="someDesc",
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



