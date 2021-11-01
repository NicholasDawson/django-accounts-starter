from django.db import models
from django.contrib.auth.models import User

# Make email address be unique for a User
User._meta.get_field('email')._unique = True
