from django.db import models

"""
Business objects contain basic information about local businesses.
"""

class Business(models.Model):
  business_id = models.CharField(max_length=128, primary_key=True)
  name = models.CharField(max_length=128, unique=True)
  full_address = models.CharField(max_length=128, blank=True, null=True)
  city = models.CharField(max_length=128, blank=True, null=True)
  state = models.CharField(max_length=128, blank=True, null=True)
  latitude = models.FloatField(blank=True, null=True)
  longitude = models.FloatField(blank=True, null=True)
  stars = models.FloatField(blank=True, null=True)
  review_count = models.IntegerField(default=0)
  #open is a keyword in Python, so use is_open instead
  is_open = models. NullBooleanField(blank=True, null=True)
  
  def __unicode__(self):
    return self.business_id

#############################################################
## subkeys for Business
#############################################################
"""
Neighborhoods holds a foreign key to a business. 
name is the name of the neighborhood
"""
class Neighborhoods(models.Model):
  business = models.ForeignKey(Business)
  name = models.CharField(max_length=128, unique=True)
  
  def __unicode__(self):
    return self.name

class Categories(models.Model):
  business = models.ForeignKey(Business)
  name = models.CharField(max_length=128, unique=True)
  
  def __unicode__(self):
    return self.name

class Attritubes(models.Model):
  business = models.ForeignKey(Business)
  name = models.CharField(max_length=128, unique=True)
  value = models.CharField(max_length=128, blank=True, null=True)
  
  def __unicode__(self):
    return self.name

class Hours(models.Model):
  business = models.ForeignKey(Business)
  day_of_week = models.CharField(max_length=50)
  open_hour = models.TimeField(blank=True, null=True)
  close_hour = models.TimeField(blank=True, null=True)
  
  def __unicode__(self):
    return self.name
#############################################################
"""
Review objects contain the review text, the star rating, and information on votes Yelp users have cast on the review. 
"""
class User(models.Model):
  user_id = models.CharField(max_length=128, primary_key=True)
  name = models.CharField(max_length=128, unique=True)
  review_count = models.IntegerField(default=0)
  average_stars = models.FloatField(blank=True, null=True)
  yelping_since = models.DateField(blank=True, null=True)
  fans = models.IntegerField(default=0)

  def __unicode__(self):
    return self.user_id

#############################################################
## subkeys for User
#############################################################
class User_Votes(models.Model):
  user = models.ForeignKey(User)
  vote_type = models.CharField(max_length=128, unique=True)
  count = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.vote_type

class Friends(models.Model):
  user = models.ForeignKey(User)
  friend_id = models.CharField(max_length=128, unique=True)
  
  def __unicode__(self):
    return self.friend_id

class Elite(models.Model):
  user = models.ForeignKey(User)
  years_elite = models.IntegerField()
  
  def __unicode__(self):
    return self.years_elite

class Compliments(models.Model):
  user = models.ForeignKey(User)
  complement_type = models.CharField(max_length=128, unique=True)
  num_compliments_of_this_type = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.complement_type
#############################################################
"""
User objects contain aggregate information about a single user across all of Yelp (including businesses and reviews not in this dataset).
"""
class Review(models.Model):
  business = models.ForeignKey(Business)
  user_id = models.ForeignKey(User)
  username = models.CharField(max_length=128)
  review_id = models.CharField(max_length=128, primary_key=True)
  stars = models.FloatField(blank=True, null=True)
  text = models.TextField(blank=True, null=True)
  date = models.DateField(blank=True, null=True)

  def __unicode__(self):
    return self.review_id

#############################################################
## subkeys for Review
#############################################################
class Review_Votes(models.Model):
  review = models.ForeignKey(Review)
  vote_type = models.CharField(max_length=128, unique=True)
  count = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.vote_type
#############################################################