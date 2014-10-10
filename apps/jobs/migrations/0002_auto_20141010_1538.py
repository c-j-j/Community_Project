# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from apps.jobs.models import Job, Team


def create_initial_data(apps, schema_editor):
    team = Team.objects.create(name="someTeam", description="someTeamDescription", location="UK")
    team.save()

    jobA = Job.objects.create(title="someTitle", description="someDesc",
                              skills="someSkills", team=team)
    jobA.save()
    jobB = Job.objects.create(title="someOtherTitle", description="someDesc",
                              skills="someSkills", team=team)
    jobB.save()
    jobC = Job.objects.create(title="someDifferentTitle", description="someDesc",
                              skills="someSkills", team=team)
    jobC.save()


class Migration(migrations.Migration):
    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data)
    ]
