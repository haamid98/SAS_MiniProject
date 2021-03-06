# Generated by Django 2.1.7 on 2019-03-25 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0007_auto_20190325_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('department', models.CharField(default='', max_length=200)),
                ('level', models.CharField(default='', max_length=200)),
                ('requirements', models.TextField(default='')),
                ('duration', models.FloatField(default=0)),
                ('campus', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University')),
            ],
        ),
    ]
