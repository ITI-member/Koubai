from django.db import models

# Create your models here.
class DeptMaster(models.Model):
    dept_id = models.CharField('ID',max_length=10)
    dept = models.CharField('部署名',max_length=20)
    note = models.CharField('備考',max_length=30)