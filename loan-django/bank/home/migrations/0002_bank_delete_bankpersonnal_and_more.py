# Generated by Django 4.1 on 2023-07-19 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toal_budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('provide', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='bankpersonnal',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='maxmim_duration',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='minimum_duration',
        ),
        migrations.RemoveField(
            model_name='loanprovider',
            name='total_budget',
        ),
        migrations.AddField(
            model_name='loan',
            name='total_loan',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanprovider',
            name='provide_history',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.bank'),
            preserve_default=False,
        ),
    ]
