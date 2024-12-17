# Generated by Django 4.2.17 on 2024-12-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_alter_contactanswer_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='region',
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='contact.contact')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.region')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
