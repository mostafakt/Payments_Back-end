# Generated by Django 4.1.4 on 2023-01-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_paid_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]