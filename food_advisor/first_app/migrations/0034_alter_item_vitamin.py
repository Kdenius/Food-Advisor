# Generated by Django 4.2.11 on 2024-03-28 19:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0033_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='vitamin',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('K', 'K'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B6', 'B6'), ('B12', 'B12'), ('B5', 'B5'), ('B7', 'B7'), ('B9', 'B9')], max_length=100, null=True),
        ),
    ]