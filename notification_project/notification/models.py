import uuid
import pytz
from django.core.validators import RegexValidator
from django.db import models
from django_unixdatetimefield import UnixDateTimeField


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(regex='^(7+([0-9]){10})$',
                       message='Phone number must be forman: 7XXXXXXXXXX',
                       code='invalid_phone_nuber')]
        )
    mobile_operator_code = models.CharField(max_length=3)  # поле не отображалось в формах и заполнялось автоматически
    tag = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50, choices=TIMEZONES, default='UTC')
    objects = models.Manager()

    def update_mobile_operator_code(self):
        self.mobile_operator_code = models.F('phone_number'[1:3])
        self.save()

    def __str__(self):
        return self.phone_number


class Newsletter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = UnixDateTimeField()
    text = models.TextField()
    mobile_operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=50)
    end_date = UnixDateTimeField()
    objects = models.Manager()


class Message(models.Model):
    class MessageStatuses(models.TextChoices):
        not_sent = 'not_sent'
        sent = 'sent'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=8, choices=MessageStatuses.choices, default=MessageStatuses.not_sent)
    sent_date = UnixDateTimeField(verbose_name='sent date')
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')
    newsletter_id = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='messages')
    objects = models.Manager()
