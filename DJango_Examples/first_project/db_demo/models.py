from django.db import models

# Create your models here.
class Topic(models.Model):

    topic = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic

class Webpage(models.Model):

    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    web_name = models.CharField(max_length=264, unique=True)
    web_url = models.URLField(unique = True)

    def __str__(self):
        return self.web_name

class AccessRecord(models.Model):

    web_info = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
