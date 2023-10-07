from django.db import models

# Create your models here.
# Planetary & Moon Models
class Jupiter(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    diameter = models.FloatField(help_text="Diameter in kilometers")
    distance_from_sun = models.FloatField(help_text="Distance from Sun in Astronomical units")
    mass = models.FloatField(help_text="Mass relected in Earth masses")
    orbital_period = models.FloatField(help_text="Orbital period reflected in Earth days")
    rotation_period = models.FloatField(help_text="Rotational period reflected in hours")

class Moon(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    diameter = models.FloatField(help_text="Diameter in Kilometer")
    orbital_period = models.FloatField(help_text="Orbital period reflected in Earth days")
    distance_from_jupiter = models.FloatField(help_text="Average distance measured in kilometers")
    