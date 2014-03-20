from django.db import models

class Business(models.Model):
  business_id = models.CharField(max_length=128, primary_key=True)
  name = models.CharField(max_length=128, unique=True)
  full_address = models.CharField(max_length=128)
  city = models.CharField()
  state = models.CharField()
  latitude = models.FloatField()
  longitude = models.FloatField()
  stars = models.FloatField()
  review_count = models.IntegerField(default=0)
  #open is a keyword in Python, so use is_open instead
  is_open = models.BooleanField()
  
  def __unicode__(self):
    return self.business_id

#############################################################
## subkeys for Business
#############################################################
class Neighborhoods(models.Model):
  business = models.Foreignkey(Business)
  name = models.CharField(max_length=128, unique=True)
  
  def __unicode__(self):
    return self.name

class Categories(models.Model):
  business = models.Foreignkey(Business)
  name = models.CharField(max_length=128, unique=True)
  
  def __unicode__(self):
    return self.name

class Attritubes(models.Model):
  business = models.Foreignkey(Business)
  name = models.CharField(max_length=128, unique=True)
  value = models.CharField(max_length=128)
  
  def __unicode__(self):
    return self.name

class Hours(models.Model):
  business = models.Foreignkey(Business)
  day_of_week = models.CharField()
  open_hour = models.TimeField()
  close_hour = models.TimeField()
  
  def __unicode__(self):
    return self.name
#############################################################

class User(models.Model):
  user_id = models.CharField(max_length=128, primary_key=True)
  name = models.CharField(max_length=128, unique=True)
  review_count = models.IntegerField(default=0)
  average_stars = models.FloatField()
  yelping_since = date = models.DateField()
  fans = models.IntegerField(default=0)

  def __unicode__(self):
    return self.user_id

#############################################################
## subkeys for User
#############################################################
class User_Votes(models.Model):
  user = models.Foreignkey(User)
  vote_type = models.CharField(max_length=128, unique=True)
  count = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.vote_type

class Friends(models.Model):
  user = models.Foreignkey(User)
  user_id = models.CharField(max_length=128, unique=True)
  
  def __unicode__(self):
    return self.user_id

class Elite(models.Model):
  user = models.Foreignkey(User)
  years_elite = models.IntegerField()
  
  def __unicode__(self):
    return self.years_elite

class Compliments(models.Model):
  user = models.Foreignkey(User)
  complement_type = models.CharField(max_length=128, unique=True)
  num_compliments_of_this_type = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.complement_type
#############################################################

class Review(models.Model):
  business = models.ForeignKey(Business)
  user = models.ForeignKey(User)
  review_id = models.CharField(max_length=128, primary_key=True)
  stars = models.FloatField()
  text = models.TextField()
  date = models.DateField()

  def __unicode__(self):
    return self.review_id

#############################################################
## subkeys for Review
#############################################################
class Review_Votes(models.Model):
  review = models.Foreignkey(Review)
  vote_type = models.CharField(max_length=128, unique=True)
  count = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.vote_type
#############################################################




