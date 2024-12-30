# Generated by Django 5.1.2 on 2024-12-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAPILog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('endpoint', models.CharField(max_length=5000)),
                ('third_party', models.CharField(blank=True, choices=[('Moralis', 'Moralis'), ('Kyber', 'Kyber')], max_length=10, null=True)),
                ('service_name', models.CharField(blank=True, max_length=100, null=True)),
                ('request_data', models.JSONField(blank=True, null=True)),
                ('response_data', models.JSONField(blank=True, null=True)),
                ('status_code', models.SmallIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('success', 'Success'), ('fail', 'Fail')], max_length=10, null=True)),
            ],
            options={
                'ordering': ('-pk',),
                'abstract': False,
            },
        ),
    ]