# Generated by Django 5.0.6 on 2024-07-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Reject', 'Reject')], default='Pending', max_length=50),
        ),
    ]
