import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Basemodel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  username = models.CharField(max_length=150, unique=False, null=True, blank=True)
  first_name = models.CharField(max_length=150, null=True, blank=True)
  last_name = models.CharField(max_length=150, null=True, blank=True)
  mobile_number = models.CharField(max_length=15, null=True, blank=True)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]

  def __str__(self) -> str:
    return self.email

class Products(Basemodel):
  CATEGORY_CHOICES = [
    ('topwear', 'Topwear'),
    ('bottomwear', 'Bottomwear'),
  ]

  CATEGORY_GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
  ]

  SUB_CATEGORY_CHOICES = [
    ('shirt', 'Shirt'),
    ('tshirt', 'T-Shirt'),
    ('blouse', 'Blouse'),
    ('sweater', 'Sweater'),
    ('hoodie', 'Hoodie'),
    ('jacket', 'Jacket'),
    ('coat', 'Coat'),
    ('crop_top', 'Crop Top'),
    ('pants', 'Pants'),
    ('jeans', 'Jeans'),
    ('shorts', 'Shorts'),
    ('skirt', 'Skirt'),
    ('leggings', 'Leggings'),
    ('trousers', 'Trousers'),
    ('kurta', 'Kurta'),
    ('kurti', 'Kurti'),
    ('sherwani', 'Sherwani'),
    ('lehenga', 'Lehenga'),
    ('saree', 'Saree'),
    ('salwar_kameez', 'Salwar Kameez'),
    ('dhoti', 'Dhoti'),
    ('maxi_dress', 'Maxi Dress'),
    ('mini_dress', 'Mini Dress'),
    ('gown', 'Gown'),
    ('jumpsuit', 'Jumpsuit'),
    ('romper', 'Romper'),
    ('underwear', 'Underwear'),
    ('lingerie', 'Lingerie'),
    ('bras', 'Bras'),
    ('boxers', 'Boxers'),
    ('briefs', 'Briefs'),
    ('sports_bra', 'Sports Bra'),
    ('track_pants', 'Track Pants'),
    ('joggers', 'Joggers'),
    ('gym_shorts', 'Gym Shorts'),
    ('sports_tshirt', 'Sports T-Shirt'),
    ('sneakers', 'Sneakers'),
    ('sandals', 'Sandals'),
    ('boots', 'Boots'),
    ('heels', 'Heels'),
    ('flats', 'Flats'),
    ('loafers', 'Loafers'),
      # Add all male and female categories
  ]

  SIZE_CATEGORY_CHOICES = [
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
  ]

  product_name = models.CharField(max_length=255)
  category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
  category_gender = models.CharField(max_length=50, choices=CATEGORY_GENDER_CHOICES)
  sub_category = models.CharField(max_length=50, choices=SUB_CATEGORY_CHOICES)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  size = models.CharField(max_length=50, choices=SIZE_CATEGORY_CHOICES)
  image = models.ImageField(upload_to='product_images/')

  def __str__(self) -> str:
    return self.product_name
