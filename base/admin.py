from django.contrib import admin
from django.contrib.auth.models import Group, User
from base.models import Book, Card, Record

# Register your models here.
admin.site.register(Card)
admin.site.register(Book)
admin.site.register(Record)
admin.site.unregister(Group)
admin.site.unregister(User)
