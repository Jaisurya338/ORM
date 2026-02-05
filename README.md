# Ex01 Django ORM Web Application
## Date: 04\02\26

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
admin.py:
```
from django.contrib import admin
from .models import swiggy_db,swiggyAdmin_db
admin.site.register(swiggy_db,swiggyAdmin_db)
```
models.py
```
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
```




## OUTPUT
'''
![alt text](<Screenshot (57).png>)
'''


## RESULT
Thus the program for creating online Food delivery database using ORM hass been executed successfully.
