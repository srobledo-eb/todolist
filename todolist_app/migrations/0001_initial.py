# Generated by Django 2.2 on 2021-04-05 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('done', models.BooleanField(default=False)),
                ('user_assigned', models.CharField(max_length=30)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist_app.Priority')),
            ],
        ),
    ]