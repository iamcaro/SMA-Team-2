# Generated by Django 3.2.4 on 2021-06-28 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Details', '0004_auto_20210627_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'ordering': ['user_id']},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='postcategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Post Categories'},
        ),
        migrations.AlterModelOptions(
            name='postcomment',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Post Comments'},
        ),
        migrations.AlterModelOptions(
            name='postlike',
            options={'verbose_name_plural': 'Post Likes'},
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='read_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user_id',
        ),
        migrations.AddField(
            model_name='follower',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender_id',
        ),
        migrations.AddField(
            model_name='message',
            name='sender_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Details.postcategory'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=models.SET(None), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
