from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    class Meta:
        db_table = 'team'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Team, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('jobs:team_detail', args=[self.pk])


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    skills = models.TextField()
    team = models.ForeignKey(Team)

    class Meta:
        db_table = 'jobs'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobs:job_detail', args=[self.pk])
