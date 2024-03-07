# Generated by Django 5.0.3 on 2024-03-07 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboardly', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='depends_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dependents', to='onboardly.question'),
        ),
        migrations.RemoveField(
            model_name='question',
            name='depends_on_answer',
        ),
        migrations.AddField(
            model_name='question',
            name='depends_on_answer',
            field=models.ManyToManyField(blank=True, related_name='dependent_questions', to='onboardly.answer'),
        ),
    ]