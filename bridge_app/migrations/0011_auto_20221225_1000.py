# Generated by Django 3.2 on 2022-12-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge_app', '0010_alter_companionrequest_companion'),
    ]

    operations = [
        migrations.AddField(
            model_name='companionrequest',
            name='finish_road',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companionrequest',
            name='finish_subrub',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companionrequest',
            name='finish_town',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companionrequest',
            name='start_road',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companionrequest',
            name='start_subrub',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companionrequest',
            name='start_town',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]