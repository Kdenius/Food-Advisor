# Generated by Django 5.0.1 on 2024-02-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_item_person_gender_person_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('total_calories', models.IntegerField(null=True)),
                ('quentity', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='calories',
            field=models.IntegerField(null=True),
        ),
    ]