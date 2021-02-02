# Generated by Django 3.1.5 on 2021-01-26 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medical_clinic', '0002_auto_20210126_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('pesel', models.CharField(blank=True, max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('sex', models.CharField(blank=True, max_length=20)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField(blank=True, max_length=5000)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(blank=True, max_length=500)),
                ('dose', models.CharField(blank=True, max_length=500)),
                ('patinet_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_clinic.patienthistory')),
            ],
        ),
    ]