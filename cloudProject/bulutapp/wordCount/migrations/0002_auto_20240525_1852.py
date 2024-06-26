# Generated by Django 3.2.9 on 2024-05-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordCount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
