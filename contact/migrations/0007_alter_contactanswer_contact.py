# Generated by Django 4.2.17 on 2024-12-17 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_contact_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactanswer',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contact.contact', verbose_name='answer'),
        ),
    ]
