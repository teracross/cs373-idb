from django.contrib import admin

# Register your models here.
from OperationRepo.models import *

admin.site.register(Business)
admin.site.register(Neighborhoods)
admin.site.register(Categories)
admin.site.register(Attributes)
admin.site.register(Hours)
admin.site.register(User)
admin.site.register(User_Votes)
admin.site.register(Elite)
admin.site.register(Compliments)
admin.site.register(Review)
admin.site.register(Review_Votes)