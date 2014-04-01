from django.db import models
import json
import jsonfield
class Business(models.Model) :
    data = jsonfield.JSONField()
class Review(models.Model) :
    data = jsonfield.JSONField()
class User(models.Model) :
    data = jsonfield.JSONField()
class Tip(models.Model) :
    data = jsonfield.JSONField()
class Checkin(models.Model) :
    data = jsonfield.JSONField()