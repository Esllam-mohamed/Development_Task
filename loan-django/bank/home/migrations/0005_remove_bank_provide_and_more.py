# Generated by Django 4.2.3 on 2023-07-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_loancustomer_loandetail_loan_bank_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='provide',
        ),
        migrations.RemoveField(
            model_name='loanprovider',
            name='provide_history',
        ),
        migrations.AddField(
            model_name='bank',
            name='provider',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
