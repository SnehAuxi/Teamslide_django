# Generated by Django 2.0.7 on 2020-11-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teamslide', '0002_delete_memberform'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
            ],
        ),
    ]
