# Generated by Django 3.2 on 2022-12-25 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridge_app', '0009_companionrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companionrequest',
            name='companion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='companion', to='bridge_app.appuser'),
        ),
    ]