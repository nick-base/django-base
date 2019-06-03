from django.db import models
from django.utils.translation import gettext as _

from utils.models import BaseModel
from users.models.account import Account

__all__ = [
    'Permission',
    'Role',
    'AccountRole'
]


class Permission(BaseModel):
    code = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=512)
    long_description = models.TextField(_('Description'), null=True)
    order = models.IntegerField(null=True, default=0)
    parent_permission = models.ForeignKey('Permission', related_name="parent", null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'u_permission'
        app_label = 'users'


class Role(BaseModel):
    title = models.CharField(max_length=512)
    permissions = models.ManyToManyField('Permission', related_name="roles")
    created_account = models.ForeignKey(Account, db_column='created_account', related_name='created_role', null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'u_role'
        app_label = 'users'

    def add_permission(self,permission):
        self.permissions.add(permission)

    def add_permissions(self, *permissions):
        self.permissions.add(*permissions)


class AccountRole(BaseModel):
    account = models.ForeignKey(Account, related_name='account_role', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name='role_account', on_delete=models.CASCADE)
    created_account = models.ForeignKey(Account, db_column='created_account', related_name='created_account_role', null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'u_account_role'
        app_label = 'users'
