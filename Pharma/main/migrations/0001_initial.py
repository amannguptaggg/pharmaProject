# Generated by Django 3.2.4 on 2021-06-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=4)),
                ('city', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=10)),
                ('date_of_Birth', models.DateField()),
                ('type_of_pharmacy', models.CharField(max_length=5)),
                ('Current_Address_of_Pharmacy', models.CharField(max_length=5)),
                ('training_done_till_date', models.DateField()),
                ('Work_experience', models.CharField(max_length=5)),
                ('qualification', models.CharField(max_length=5)),
                ('IdProofNumber', models.CharField(max_length=5)),
            ],
        ),
    ]