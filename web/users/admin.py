from django.contrib import admin
from users.models import Account, Permission, Role, AccountRole

admin.site.register(Account)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(AccountRole)
