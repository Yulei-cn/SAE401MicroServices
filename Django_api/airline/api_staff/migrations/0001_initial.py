# Generated by Django 5.0.6 on 2024-06-13 22:23

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'airport',
            },
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('second_class_capacity', models.IntegerField()),
                ('first_class_capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'plane',
            },
        ),
        migrations.CreateModel(
            name='StaffType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'staff_type',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, related_name='staff_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='staff_permissions', to='auth.permission')),
                ('staff_type', models.ForeignKey(db_column='staff_type', on_delete=django.db.models.deletion.CASCADE, to='api_staff.stafftype')),
            ],
            options={
                'db_table': 'staff',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.CharField(max_length=10)),
                ('length', models.IntegerField()),
                ('airport', models.ForeignKey(db_column='airport', on_delete=django.db.models.deletion.CASCADE, to='api_staff.airport')),
            ],
            options={
                'db_table': 'track',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10, unique=True)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('plane', models.ForeignKey(db_column='plane', default=1, on_delete=django.db.models.deletion.CASCADE, to='api_staff.plane')),
                ('track_destination', models.ForeignKey(db_column='track_destination', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='track_destinations', to='api_staff.track')),
                ('track_origin', models.ForeignKey(db_column='track_origin', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='track_origins', to='api_staff.track')),
            ],
            options={
                'db_table': 'flight',
            },
        ),
    ]
