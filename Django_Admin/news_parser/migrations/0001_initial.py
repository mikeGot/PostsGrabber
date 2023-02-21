# Generated by Django 4.1.7 on 2023-02-21 16:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=128, verbose_name='tag')),
                ('date', models.DateTimeField(verbose_name='datetime')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'Posts',
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(verbose_name='url')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_parser.post')),
            ],
            options={
                'verbose_name': 'Urls',
                'db_table': 'urls',
            },
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=256, verbose_name='tag')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_parser.post')),
            ],
            options={
                'verbose_name': 'Polls',
                'db_table': 'polls',
            },
        ),
    ]
