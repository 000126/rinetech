# Generated by Django 5.0 on 2024-01-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rineapp', '0004_uploadedfile_user_alter_uploadedfile_template_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('excel_file', models.FileField(upload_to='excels/')),
            ],
        ),
    ]