from django.db import models
from django.contrib.auth.models import User

class BaseCustomModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(class)s_created")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(class)s_updated")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Bookie(BaseCustomModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookie')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SubProfile(BaseCustomModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_user_profile')
    bookie = models.ForeignKey(Bookie, on_delete=models.CASCADE, related_name='sub_profile')
    nickname = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exposure_limit = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bookie.name} - {self.nickname}"

    class Meta:
        unique_together = ['bookie', 'nickname']