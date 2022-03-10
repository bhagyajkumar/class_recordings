from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from discord_webhook import DiscordWebhook, DiscordEmbed
from django.conf import settings


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    webhook_url = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    url = models.TextField()
    brief = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)


@receiver(post_save, sender=Content)
def save_handler(sender, **kwargs):
    instance = kwargs["instance"]
    webhook = DiscordWebhook(url=instance.subject.webhook_url)
    embed = DiscordEmbed(title=f"{instance.date}-{instance.subject.name}",
                         description=f"{instance.date}\n[ Drive link]({instance.url})", color='03b2f8')
    webhook.add_embed(embed=embed)
    webhook.execute()
