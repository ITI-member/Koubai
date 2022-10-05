from operator import length_hint
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class DeptMaster(models.Model):
    dept_id = models.IntegerField('ID',validators=[MinValueValidator(1), MaxValueValidator(999)], unique=True,)
    dept = models.CharField('部署名',max_length=20,)
    note = models.CharField('備考',max_length=30, null=True, blank=True)

class PurchaserMaster(models.Model):
    place_id = models.IntegerField('ID',validators=[MinValueValidator(1), MaxValueValidator(999)], unique=True)
    place = models.CharField('購入先',max_length=20)
    note = models.CharField('備考',max_length=30, null=True, blank=True)

class ListOfPurchases(models.Model):
    item_name = models.CharField('商品名', max_length=50)
    deploy_id = models.CharField('部署ID', max_length=100)
    store_id = models.CharField('購入先ID', max_length=100)
    user_id = models.CharField('担当者名',max_length=50, null=True, blank=True)
    unit_prise = models.IntegerField('単価')
    quantity = models.IntegerField('数量')
    total_due = models.IntegerField('金額')
    remarks = models.CharField('備考',max_length=50, null=True, blank=True)
    insert_date_time = models.DateTimeField('登録日時',auto_now_add=True)
    update_date_time = models.DateTimeField('更新日時',auto_now=True)
