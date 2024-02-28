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