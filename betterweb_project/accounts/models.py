from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaLanguageBaseProfile

class BetterWebProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User)