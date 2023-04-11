# Generated by Django 3.2.11 on 2023-04-10 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reaction', models.IntegerField(choices=[(1, 'like'), (-1, 'dislike')], verbose_name='like-dislike')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_reactions', to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'article', 'reaction')},
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
