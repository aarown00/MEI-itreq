# Generated by Django 5.0.6 on 2024-05-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_it_request_issue_alter_it_request_pc_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='it_request',
            name='pc_type',
        ),
        migrations.AddField(
            model_name='it_request',
            name='eq_type',
            field=models.CharField(choices=[('Desktop', 'Desktop'), ('Laptop', 'Laptop'), ('Others', 'Others')], default='Desktop', max_length=10),
        ),
        migrations.AlterField(
            model_name='it_request',
            name='issue',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Network', 'Network')], default='Software', max_length=10),
        ),
        migrations.AlterField(
            model_name='it_request',
            name='status',
            field=models.CharField(choices=[('Requested', 'Requested'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Requested', max_length=10),
        ),
    ]