from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        if extra_fields.get('is_admin') is not True:
            raise ValueError(_('Superuser must have is_admin=True'))
        return self.create_user(username,password,**extra_fields)
