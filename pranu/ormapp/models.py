from django.db import models
from django.contrib import admin
class swiggy_db(models.Model):
	orderNo=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=10)
	ratings=models.FloatField()
	cuisine=models.TextField()
	Email=models.EmailField()
	address=models.CharField()
	Mobile_no=models.IntegerField()
class swiggyAdmin_db(admin.ModelAdmin):
	list_display=['orderNo','Name','ratings','cuisine','Email','address','Mobile_no']


