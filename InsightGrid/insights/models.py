from django.db import models

# Create your models here.

class Insight(models.Model):
    intensity = models.IntegerField(null=True, blank=True)
    likelihood = models.IntegerField(null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)

    year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)

    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)

    topics = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    pestle = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    swot = models.CharField(max_length=255, null=True, blank=True)

    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year']
        indexes = [
            models.Index(fields=['country']),
            models.Index(fields=['year']),
            models.Index(fields=['topics']),
            models.Index(fields=['sector']),
            models.Index(fields=['region']),
            models.Index(fields=['end_year']),
            models.Index(fields=['country', 'year']),
        ]

    def __str__(self):
        return f"{self.topics} - {self.country}"