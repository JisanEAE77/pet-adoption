from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    SPECIES_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('rabbit', 'Rabbit'),
        ('bird', 'Bird'),
        ('horse', 'Horse'),
        ('hamster', 'Hamster'),
        ('guinea_pig', 'Guinea Pig'),
        ('snake', 'Snake'),
        ('turtle', 'Turtle'),
        ('fish', 'Fish'),
        ('other', 'Other'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),
    )

    SIZE_CHOICES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )

    BEHAVIOR_CHOICES = (
        ('tamed', 'Tamed'),
        ('wild', 'Wild'),
        ('friendly', 'Friendly'),
        ('aggressive', 'Aggressive'),
        ('calm', 'Calm'),
    )

    HEALTH_CHOICES = (
        ('healthy', 'Healthy'),
        ('injured', 'Injured'),
        ('sick', 'Sick'),
        ('special_needs', 'Special Needs'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_adopted = models.BooleanField(default=False)
    adopted_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    behavior = models.CharField(max_length=20, choices=BEHAVIOR_CHOICES, blank=True, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='pet_photos/')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=255)
    vaccinated = models.BooleanField(default=False)
    dewormed = models.BooleanField(default=False)
    neutered_spayed = models.BooleanField(default=False)
    microchipped = models.BooleanField(default=False)
    friendly_with_kids = models.BooleanField(default=False)
    friendly_with_dogs = models.BooleanField(default=False)
    friendly_with_cats = models.BooleanField(default=False)
    special_needs = models.TextField(blank=True, null=True)
    adoption_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    coat_length = models.CharField(max_length=50, blank=True, null=True)
    eye_color = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    health_status = models.CharField(max_length=20, choices=HEALTH_CHOICES, default='healthy')

    def __str__(self):
        return self.name
