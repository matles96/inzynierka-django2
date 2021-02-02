# Generated by Django 3.1.5 on 2021-01-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_clinic', '0003_patient_patienthistory_prescription_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='dose',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='medicine',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
    ]