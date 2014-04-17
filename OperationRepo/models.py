from django.db import models

DAYS = (
  ('Mon', 'Monday'),
  ('Tue', 'Tuesday'),
  ('Wed', 'Wednesday'),
  ('Thur', 'Thursday'),
  ('Fri', 'Friday'),
  ('Sat', 'Saturday'),
  ('Sun', 'Sunday'),
)
  """Enum to represent day_of_week."""

class Business(models.Model):
  """
  Business objects contain basic information about local businesses.
  Each businesses has a set of 'Review'. 
  """
  business_id = models.CharField(max_length=128, primary_key=True)
  name = models.CharField(max_length=128)
  full_address = models.CharField(max_length=128, blank=True, null=True)
  city = models.CharField(max_length=128, blank=True, null=True)
  state = models.CharField(max_length=128, blank=True, null=True)
  latitude = models.FloatField(blank=True, null=True)
  longitude = models.FloatField(blank=True, null=True)
  stars = models.FloatField(blank=True, null=True)
  review_count = models.IntegerField(default=0)
  is_open = models.NullBooleanField(blank=True, null=True)
  yelp_url = models.URLField(blank=True, null=True, max_length=200);
  
  def __unicode__(self):
    return self.business_id

#############################################################
## subkeys for Business
#############################################################
class Categories(models.Model):
  """
  A multivalued attribute for Business representing what category the business belongs to.
  """
  business = models.ForeignKey(Business)
  name = models.CharField(max_length=128)
  
  def __unicode__(self):
    return self.name

class Attributes(models.Model):
  """
  A multivalued attribute for Business containing all of the additional features the business has.
  """
  business = models.ForeignKey(Business)
  name = models.CharField(max_length=128)
  value = models.TextField(blank=True, null=True)
  
  def __unicode__(self):
    return self.name

class Hours(models.Model):
  """
  A multivalued attribute for Business representing the business hour of the business.
  """
  business = models.ForeignKey(Business)
  day_of_week = models.CharField(max_length=50, choices=DAYS)
  open_hour = models.TimeField(blank=True, null=True)
  close_hour = models.TimeField(blank=True, null=True)
#############################################################

class User(models.Model):
  """
  User objects contain aggregate information about a single user across all of Yelp (including businesses and reviews not in this dataset).
  Each user has a set of Review.
  """
  user_id = models.CharField(max_length=128, primary_key=True)
  name = models.CharField(max_length=128)
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
  """
  A multivalued attribute for User representing the different type of vote the user has and the counts of each type of vote.
  """
  user = models.ForeignKey(User)
  vote_type = models.CharField(max_length=128)
  count = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.vote_type

class Elite(models.Model):
  """
  A multivalued attribute for User containing the years that the user is elite.
  """
  user = models.ForeignKey(User)
  years_elite = models.IntegerField()
  
  def __unicode__(self):
    return self.years_elite

class Compliments(models.Model):
  """
  A multivalued attribute for User containing all of the different compliments the user gave and the count of each compliments.
  """
  user = models.ForeignKey(User)
  complement_type = models.CharField(max_length=128)
  num_compliments_of_this_type = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.complement_type
#############################################################

class Review(models.Model):
  """
  Review objects contain the review text, the star rating, and information on votes Yelp users have cast on the review. 
  Each review is written by a User for a Business
  """
  business = models.ForeignKey(Business)
  user = models.ForeignKey(User)
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
  """
  A multivalued attribute for Review representing the different type of vote the review has and the counts of each type of vote.
  """
  review = models.ForeignKey(Review)
  vote_type = models.CharField(max_length=128)
  count = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.vote_type
#############################################################