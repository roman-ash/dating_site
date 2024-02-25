import uuid
from django.core.validators import RegexValidator
from django.db import models
from django_unixdatetimefield import UnixDateTimeField


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(regex='^(7+([0-9]){10})$',
                       message='Phone number must be forman: 7XXXXXXXXXX',
                       code='invalid_phone_nuber')]
        )
    mobile_operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=10)
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
    end_date = UnixDateTimeField()
    objects = models.Manager()

class Message(models.Model):
    class AccountStatuses(models.TextChoices):
        sent = 'sent'
        not_sent = 'not_sent'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = UnixDateTimeField()
