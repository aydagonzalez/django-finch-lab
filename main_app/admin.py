from django.contrib import admin
# add Feeding to the import
from .models import Cat, Feeding

# Register your models here.
from .models import Cat
admin.site.register(Cat)
admin.site.register(Feeding)
