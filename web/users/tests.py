from django.test import TestCase
from users.models import *

class PermissionTestCase(TestCase):
    def setUp(self):
        self.role = Role.objects.create(title="Admin")
        self.permission = Permission.objects.create(code="perms.users", description="")
        self.role.permissions.add(self.permission)

        self.account = Account.objects.create(name="User1")
        AccountRole.objects.create(account=self.account, role=self.role)

    def test_animals_can_speak(self):
        self.assertEqual(self.account.has_perm("perms.users"), True)
        self.assertEqual(self.account.has_perm("perms.users.view"), False)
