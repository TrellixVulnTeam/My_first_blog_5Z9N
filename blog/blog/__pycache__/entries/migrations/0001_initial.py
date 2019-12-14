# Generated by Django 2.2.7 on 2019-11-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.CharField(max_length=50)),
                ('entry_text', models.TextField()),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
