# Generated by Django 2.2.5 on 2019-09-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(help_text='Nazwa pizzy', max_length=30, verbose_name='pizza')),
                ('opis', models.TextField(blank=True, help_text='Opis pizzy')),
                ('rozmiar', models.CharField(choices=[('L', 'duża'), ('M', 'średnia'), ('S', 'mała')], default='L', max_length=1)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField(auto_now_add=True, verbose_name='dodano')),
            ],
        ),
        migrations.CreateModel(
            name='Skladnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='składnik')),
                ('jarski', models.BooleanField(default=False, help_text='Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian,', verbose_name='jarski?')),
                ('cena', models.DecimalField(decimal_places=2, max_digits='3')),
                ('pizza', models.ManyToManyField(related_name='skladniki', to='pizza.Pizza')),
            ],
        ),
    ]