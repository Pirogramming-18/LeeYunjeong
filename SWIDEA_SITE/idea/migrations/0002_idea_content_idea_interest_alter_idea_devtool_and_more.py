# Generated by Django 4.1.5 on 2023-01-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='interest',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.CharField(choices=[('django', 'django'), ('react', 'react'), ('Spring', 'Spring'), ('Node.js', 'Node.js'), ('Java', 'Java'), ('C++', 'C++')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='image',
            field=models.ImageField(null=True, upload_to='idea'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]