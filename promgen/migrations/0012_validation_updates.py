# Copyright (c) 2020 LINE Corporation
# These sources are released under the terms of the MIT license: see LICENSE
# Generated by Django 2.2.9 on 2020-01-16 06:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("promgen", "0011_notifier_counts")]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="name",
            field=models.CharField(
                max_length=128,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z_]*$", "Only alphanumeric characters are allowed."
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(
                max_length=128,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z_]*$", "Only alphanumeric characters are allowed."
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(
                max_length=128,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z_]*$", "Only alphanumeric characters are allowed."
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="shard",
            name="name",
            field=models.CharField(
                max_length=128,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z_]*$", "Only alphanumeric characters are allowed."
                    )
                ],
            ),
        ),
    ]
