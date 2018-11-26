# Generated by Django 2.0.8 on 2018-11-14 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181114_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('zip', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='workshop',
            name='category',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Workshop'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Location'),
        ),
    ]
