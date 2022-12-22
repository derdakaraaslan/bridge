# Generated by Django 3.2 on 2022-12-22 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bridge_app', '0002_appuser_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EquipmentHelp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('comment', models.TextField()),
                ('share_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bridge_app.equipmenttype')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bridge_app.appuser')),
            ],
        ),
    ]
