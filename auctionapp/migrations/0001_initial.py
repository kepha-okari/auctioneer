# Generated by Django 2.1.5 on 2019-02-10 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='photos/')),
                ('is_sold', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=200, null=True)),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionapp.Artifact')),
            ],
        ),
    ]
