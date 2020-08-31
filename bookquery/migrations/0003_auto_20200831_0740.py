# Generated by Django 3.1 on 2020-08-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookquery', '0002_bookquery_any_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookquery',
            name='any_field',
            field=models.CharField(max_length=1000, verbose_name='Enter as many keywords about the book as possible'),
        ),
    ]