from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from discord_webhook import DiscordWebhook, DiscordEmbed
from django.conf import settings


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


@receiver(post_save, sender=Content)
def save_handler(sender, **kwargs):
    webhook = DiscordWebhook(url=settings.DISCORD_WEBHOOK_URL)
    instance = kwargs["instance"]
    embed = DiscordEmbed(title=f"{instance.date}-{instance.subject.name}",
                         description=f"{instance.date}\n[ Drive link]({instance.url})", color='03b2f8')
    webhook.add_embed(embed=embed)
    webhook.execute()
