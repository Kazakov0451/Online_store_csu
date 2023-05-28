from django.db import models
from django.urls import reverse


class Customers(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    number_phone = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name


class Vendors(models.Model):
    id_vendor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Products(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='media/')
    article_number = models.IntegerField(unique=True)
    description = models.TextField()
    composition = models.TextField()

    def __str__(self):
        return self.name

    def get_url(self):
        """
        Get to go to product detail page.
        :return: reverse url for particular product
        """
        return reverse('product_detail', args=[self.category, self.slug])


class ProductSize(models.Model):
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_size")
    size = models.FloatField(primary_key=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id_product)


class Price(models.Model):
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="price")
    date_price_changed = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    def __str__(self):
        return str(self.id_product)


class Sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="sale")
    date_sale = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_customer)


class Incoming(models.Model):
    id_vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name="incoming")
    date_incoming = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_vendor)


class MagazineSales(models.Model):
    id_sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="magazine_sales")
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="magazine_sales_products")
    size = models.FloatField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_sale)


class MagazineIncoming(models.Model):
    id_incoming = models.ForeignKey(Incoming, on_delete=models.CASCADE, related_name="magazine_incoming")
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="magazine_incoming_product")
    size = models.FloatField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_incoming)
