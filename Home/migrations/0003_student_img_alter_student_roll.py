# Generated by Django 5.0.3 on 2024-04-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_exam_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]