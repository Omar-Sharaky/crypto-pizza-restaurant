# Generated by Django 3.0.6 on 2020-06-01 16:03
#importing migrations & models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_dinner_platter_pasta_salad_sub_topping'),
    ]
#creating new model "foodtpe" with 2 fields (id, name)   
    operations = [
        migrations.CreateModel(
            name='foodtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]