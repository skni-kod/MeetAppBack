# Generated by Django 4.0.5 on 2022-06-19 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Event_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('x', models.FloatField(default=0)),
                ('y', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/default.jpeg', null=True, upload_to='profiles/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Profile_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile_Event_Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner', models.BooleanField(default=False)),
                ('Event_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MeetApp.event')),
                ('Profile_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MeetApp.profile')),
            ],
        ),
    ]
