from django.db import models


class Message(models.Model):
    header = models.CharField(max_length=255, null=True, blank=True)
    msg_body = models.TextField(max_length=500, null=True, blank=True)
    is_send = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        db_table = 'messages'
