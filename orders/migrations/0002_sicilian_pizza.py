# Generated by Django 3.0.6 on 2020-05-31 20:12

#importing migrations & models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]
    #creating new model "Sicilian_pizza with 4 fields (id, name, small price, large price)"
    operations = [
        migrations.CreateModel(
            name='Sicilian_pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.DecimalField(decimal_places=2, max_digits=4)),
                ('large', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
