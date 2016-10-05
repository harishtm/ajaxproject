from django.contrib import admin
from country.models import *


admin.site.register(MyCountry)
admin.site.register(State)
admin.site.register(District)

