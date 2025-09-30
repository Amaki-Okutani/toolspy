from django.db import models


class TsnTools(models.Model):
    product_group_code = models.CharField(primary_key=True,max_length=3)
    product_group_name = models.CharField(max_length=128)
    product_group_abbreviation = models.CharField(max_length=15,null=True,blank=True)
    domestic_abroad_class = models.CharField(max_length=1)
    created_by = models.CharField(max_length=16,null=True,blank=True)
    created_datetime =models.DateTimeField()
    updated_by = models.CharField(max_length=16,null=True,blank=True)
    updated_datetime = models.DateTimeField()
    class Meta:
        db_table='product_groups'
        managed = False