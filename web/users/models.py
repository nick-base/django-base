from django.db import models
from django.utils.translation import gettext as _

from utils.models import BaseModel
from users.constant import PERMISSION_DIC

class Account(BaseModel): 
    mobile = models.CharField(max_length=32, null=True, blank=True)
    email_address = models.EmailField(max_length=64, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null = True, blank = True)
    first_name = models.CharField(max_length=128, null = True, blank = True)
    last_name = models.CharField(max_length=128, null = True, blank = True)
    active = models.BooleanField(default=False)
    status = models.CharField(max_length=1,default='1')
    password_reset_code = models.CharField(max_length=40, null=True, blank=True)
    password_reset_code_create_time = models.DateTimeField(null=True, blank=True)
    email_reset_code = models.CharField(max_length=40, null=True, blank=True)
    email_reset_code_create_time = models.DateTimeField(null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'u_account'
        app_label = 'users'

    def get_roles(self):
        return [account_role.role for account_role in self.account_role.all()]

    def get_perms(self):
        """
        Return:
            permission code list, item (string)
        """
        if not getattr(self, "_perms", None) or not self._perms:
            self._perms = {}.fromkeys(list(self.account_role.all().values_list("role__permissions__code", flat=True))).keys()
        return self._perms

    def has_perm(self, perm):
        """
        Args: 
            perm: permission code (string)
        """
        if not perm in PERMISSION_DIC:
            raise Exception("The permission code is error")
        perm = PERMISSION_DIC.get(perm)
        perms = self.get_perms()
        if perm in perms:
            return True
        return False

    def has_perms(self, *perms):
        """
        Args 
            perms: list of permission code
        """
        return all(map(lambda perm: self.has_perm(perm), perms))


class Permission(BaseModel):
    code = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=512)
    long_description = models.TextField(_('Description'), null=True)
    order=models.IntegerField(null=True, default=0)
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

__all__ = [
    'Account',
    'Permission',
    'Role',
    'AccountRole'
]
