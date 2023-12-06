from django.db import models

# Create your models here.


class Meeting(models.Model):

    topic = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = ("Meeting")
        verbose_name_plural = ("Meetings")

    def get_absolute_url(self):
        return reverse("Meeting_detail", kwargs={"pk": self.pk})
