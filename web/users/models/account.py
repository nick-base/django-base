from django.db import models
from django.utils.translation import gettext as _

from utils.models import BaseModel
from users.constant import PERMISSION_DIC

__all__ = [
    'Account',
]


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
    token = models.CharField(max_length=128, null = True, blank = True)
    token_create_time = models.DateTimeField(null=True, blank=True)

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
