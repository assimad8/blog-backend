# Generated by Django 5.1.7 on 2025-03-22 12:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='posts/videos/')),
                ('file', models.FileField(blank=True, null=True, upload_to='posts/files/')),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('likes_count', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core_post.category')),
                ('tags', models.ManyToManyField(blank=True, to='core_post.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
