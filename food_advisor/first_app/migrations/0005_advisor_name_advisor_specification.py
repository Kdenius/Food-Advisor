# Generated by Django 5.0 on 2024-02-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_remove_advisor_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='advisor',
            name='specification',
            field=models.TextField(null=True),
        ),
    ]