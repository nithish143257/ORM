# Ex02 Django ORM Web Application
## Date: 28/02/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![image](https://github.com/nithish143257/ORM/assets/113762839/600ba062-d9c9-46ab-a8d8-64aa89a2879f)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
admin.py

from django.contrib import admin
from.models import Book_DB,Book_DBAdmin
admin.site.register(Book_DB,Book_DBAdmin)

models.py

from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
    b_id = models.IntegerField(primary_key="b_id");
    b_name = models.CharField(max_length=100);
    b_author = models.CharField(max_length=100);
    b_edition = models.CharField(max_length=20);
    b_year = models.DateField();

class Book_DBAdmin(admin.ModelAdmin):
    list_display = ("b_id","b_name","b_author","b_edition","b_year");
```

## OUTPUT

![alt text](<Screenshot (128).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
