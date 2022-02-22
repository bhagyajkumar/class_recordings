from django.db import models


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.name


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    url = models.TextField()
    brief = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
