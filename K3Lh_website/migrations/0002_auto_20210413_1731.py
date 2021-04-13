# Generated by Django 3.1.7 on 2021-04-13 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('K3Lh_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keadaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='kotak',
            name='keadaan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='K3Lh_website.keadaan'),
        ),
    ]
