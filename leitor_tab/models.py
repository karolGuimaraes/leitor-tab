from django.db import models

class Sale(models.Model):
    purchaser_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    purchase_count = models.IntegerField(default=0)
    merchant_address = models.CharField(max_length=200)
    merchant_name = models.CharField(max_length=200)

    def __str__(self):
        return "Purchaser {} Item {} Price {} Count {} Address {} Merchant {}".format(self.purchaser_name, 
                                                                                      self.item_description,
                                                                                      self.item_price,
                                                                                      self.purchase_count,
                                                                                      self.merchant_address,
                                                                                      self.merchant_name)
