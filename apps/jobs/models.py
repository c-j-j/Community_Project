from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'team'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + self.location)
        super(Team, self).save(*args, **kwargs)


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