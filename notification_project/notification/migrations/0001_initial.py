# Generated by Django 2.2.28 on 2024-02-24 16:05

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_phone_nuber', message='Phone number must be 7XXXXXXXXXX', regex='^(7+([0-9]){10})$')])),
                ('mobile_operator_code', models.CharField(max_length=3)),
            ],
        ),
    ]