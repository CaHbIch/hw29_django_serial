from django.contrib import admin

from users.models.location import Location
from users.models.user import User


admin.site.register(Location)
admin.site.register(User)
