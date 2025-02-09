# Generated by Django 4.1.2 on 2024-04-17 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0002_scoringtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='crif',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='scoring.crif', verbose_name='parent'),
        ),
        migrations.AddField(
            model_name='crif',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='scoring.scoringtype', verbose_name='type'),
            preserve_default=False,
        ),
    ]
