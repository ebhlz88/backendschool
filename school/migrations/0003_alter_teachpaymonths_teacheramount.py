# Generated by Django 3.2 on 2021-07-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_marks_subjectmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachpaymonths',
            name='teacheramount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
