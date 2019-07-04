# Generated by Django 2.2.1 on 2019-06-01 11:27

from django.db import migrations, models
import django.db.models.deletion
import util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default=None, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=9)),
                ('cover', models.ImageField(default=None, upload_to=util.customize_foldername)),
                ('available', models.BooleanField(default=True)),
                ('bpm', models.IntegerField(default=None)),
                ('track', models.FileField(default=None, upload_to='')),
                ('tonality', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Beats',
                'verbose_name': 'Beat',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default=None, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('beat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Beat')),
            ],
            options={
                'verbose_name_plural': 'Cart Items',
                'verbose_name': 'Cart Item',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('beats', models.ManyToManyField(blank=True, to='mainApp.CartItem')),
            ],
            options={
                'verbose_name_plural': 'Carts',
                'verbose_name': 'Cart',
            },
        ),
        migrations.AddField(
            model_name='beat',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Category'),
        ),
    ]
