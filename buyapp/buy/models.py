from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class DeptMaster(models.Model):
    id = models.AutoField(primary_key=True)
    dept_id = models.IntegerField('ID',validators=[MinValueValidator(1), MaxValueValidator(999)], unique=True,)
    dept = models.CharField('部署名',max_length=20,)
    note = models.CharField('備考',max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.dept
    

class PurchaserMaster(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField('ID',validators=[MinValueValidator(1), MaxValueValidator(999)], unique=True)
    place = models.CharField('購入先',max_length=20)
    note = models.CharField('備考',max_length=30, null=True, blank=True)

    def __str__(self):
        return self.place
    

class ListOfPurchases(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField('商品名', max_length=50)
    dept = models.ForeignKey(DeptMaster, on_delete=models.PROTECT)
    store = models.ForeignKey(PurchaserMaster, on_delete=models.PROTECT)
    user_id = models.CharField('担当者名',max_length=50, null=True, blank=True)
    order_day = models.DateField('注文日')
    order_plan = models.IntegerField('注文予定日',null=True, blank=True)
    unit_prise = models.IntegerField('単価')
    quantity = models.IntegerField('数量')
    total_due = models.IntegerField('金額')
    remarks = models.CharField('備考',max_length=50, null=True, blank=True)
    insert_date_time = models.DateTimeField('登録日時',auto_now_add=True)
    update_date_time = models.DateTimeField('更新日時',auto_now=True)

    def __str__(self):
        return '{0}{1}'.format(self.dept,self.store)
