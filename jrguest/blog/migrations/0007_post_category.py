# Generated by Django 3.2.6 on 2022-01-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220107_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Website Development', max_length=255),
        ),
    ]
