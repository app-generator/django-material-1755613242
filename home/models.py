# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    passwork = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Orders(models.Model):

    #__Orders_FIELDS__
    order_id = models.CharField(max_length=255, null=True, blank=True)
    order_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    receive_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    channel = models.CharField(max_length=255, null=True, blank=True)
    platform = models.CharField(max_length=255, null=True, blank=True)
    cust_uname = models.CharField(max_length=255, null=True, blank=True)
    recipient_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    process = models.CharField(max_length=255, null=True, blank=True)
    remark = models.TextField(max_length=255, null=True, blank=True)

    #__Orders_FIELDS__END

    class Meta:
        verbose_name        = _("Orders")
        verbose_name_plural = _("Orders")


class Order_Details(models.Model):

    #__Order_Details_FIELDS__
    order_id = models.ForeignKey(orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    selling_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    batch_id = models.CharField(max_length=255, null=True, blank=True)

    #__Order_Details_FIELDS__END

    class Meta:
        verbose_name        = _("Order_Details")
        verbose_name_plural = _("Order_Details")


class Products(models.Model):

    #__Products_FIELDS__
    product_id = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    selling_price = models.IntegerField(null=True, blank=True)
    current_stock = models.IntegerField(null=True, blank=True)
    min_stock = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Batches(models.Model):

    #__Batches_FIELDS__
    batch_id = models.CharField(max_length=255, null=True, blank=True)
    import_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Batches_FIELDS__END

    class Meta:
        verbose_name        = _("Batches")
        verbose_name_plural = _("Batches")


class Batch_Details(models.Model):

    #__Batch_Details_FIELDS__
    batch_id = models.ForeignKey(batches, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    unit_cost = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    remain = models.IntegerField(null=True, blank=True)

    #__Batch_Details_FIELDS__END

    class Meta:
        verbose_name        = _("Batch_Details")
        verbose_name_plural = _("Batch_Details")


class Transactions(models.Model):

    #__Transactions_FIELDS__
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    category = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    from_account = models.CharField(max_length=255, null=True, blank=True)
    to_account = models.CharField(max_length=255, null=True, blank=True)
    confirm = models.BooleanField()
    note = models.TextField(max_length=255, null=True, blank=True)

    #__Transactions_FIELDS__END

    class Meta:
        verbose_name        = _("Transactions")
        verbose_name_plural = _("Transactions")



#__MODELS__END
