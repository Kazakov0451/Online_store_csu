# Generated by Django 4.1.6 on 2023-05-25 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id_customer', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('number_phone', models.CharField(max_length=14, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_incoming', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='media/')),
                ('article_number', models.IntegerField(unique=True)),
                ('description', models.TextField()),
                ('composition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id_vendor', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id_sale', models.AutoField(primary_key=True, serialize=False)),
                ('date_sale', models.DateTimeField(auto_now_add=True)),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale', to='main.customers')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('size', models.FloatField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='main.products')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_price_changed', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='main.products')),
            ],
        ),
        migrations.CreateModel(
            name='MagazineSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.FloatField()),
                ('quantity', models.IntegerField(default=0)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazine_sales_products', to='main.products')),
                ('id_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazine_sales', to='main.sale')),
            ],
        ),
        migrations.CreateModel(
            name='MagazineIncoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.FloatField()),
                ('quantity', models.IntegerField(default=0)),
                ('id_incoming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazine_incoming', to='main.incoming')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazine_incoming_product', to='main.products')),
            ],
        ),
        migrations.AddField(
            model_name='incoming',
            name='id_vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming', to='main.vendors'),
        ),
    ]