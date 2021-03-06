# Generated by Django 4.0.6 on 2022-07-09 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.FileField(upload_to='icons/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='action_image')),
                ('language', models.CharField(choices=[('en-IN-PrabhatNeural', 'English Male'), ('en-IN-NeerjaNeural', 'English Female'), ('hi-IN-MadhurNeural', 'Hindi Male'), ('hi-IN-SwaraNeural', 'Hindi Female'), ('gu-IN-NiranjanNeural', 'Gujarati Male'), ('gu-IN-DhwaniNeural', 'Gujarati Female')], default='en-IN-PrabhatNeural', max_length=40)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.actioncategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActionVoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('voice', models.FileField(upload_to='action_voice')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.actiondetail')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
