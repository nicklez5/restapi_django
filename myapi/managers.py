from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username,password=password)