# Generated by Django 4.2.11 on 2024-03-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0032_alter_item_vitamin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('F', 'fruit'), ('V', 'vegetable'), ('J', 'junk_food'), ('D', 'dairy product'), ('S', 'sweets')], max_length=1),
        ),
    ]
