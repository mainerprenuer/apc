# Generated by Django 3.2.13 on 2022-10-10 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.lga')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('acc_num', models.IntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.lga')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.state')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ward')),
            ],
        ),
        migrations.AddField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.state'),
        ),
    ]
