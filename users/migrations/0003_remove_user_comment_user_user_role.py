# Generated by Django 4.1.2 on 2023-12-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='comment',
        ),
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('credit-officer', 'Кредитный офицер'), ('underwriter', 'Андерайтер'), ('operation-officer', 'Операционный офицер'), ('call-officer', 'Агент колл-центра')], default='credit-officer', max_length=50, verbose_name='docx template name'),
        ),
    ]
