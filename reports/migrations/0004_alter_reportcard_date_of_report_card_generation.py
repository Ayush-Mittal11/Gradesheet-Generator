# Generated by Django 5.0.1 on 2024-01-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
