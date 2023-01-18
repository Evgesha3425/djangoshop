# Generated by Django 4.1.4 on 2023-01-18 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField(verbose_name='артикль')),
                ('serial_number', models.CharField(max_length=50, verbose_name='серийный номер')),
            ],
            options={
                'verbose_name_plural': 'Артикль',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(null=True, verbose_name='описание')),
                ('price', models.FloatField(null=True, verbose_name='цена')),
                ('size', models.IntegerField(verbose_name='размер')),
                ('color', models.CharField(max_length=100, null=True, verbose_name='цвет')),
                ('article', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.article')),
            ],
            options={
                'verbose_name_plural': 'Одежда',
                'ordering': ['-price'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('surname', models.CharField(max_length=100, verbose_name='фамилия')),
                ('age', models.IntegerField(verbose_name='возраст')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('adress', models.CharField(max_length=50, verbose_name='адрес')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=50, verbose_name='адрес')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('main_manager', models.CharField(max_length=50, verbose_name='Главный менеджер')),
                ('clothes', models.ManyToManyField(to='catalog.clothes')),
            ],
            options={
                'verbose_name_plural': 'Магазины',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('clothes', models.ManyToManyField(to='catalog.clothes')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.shop')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.users')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
