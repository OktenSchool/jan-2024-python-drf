from django.db import models


class BodyTypeChoices(models.TextChoices):
    HatchBack = 'HatchBack'
    Sedan = 'Sedan',
    Coupe = 'Coupe',
    Wagon = 'Wagon',
    Jeep = 'Jeep',
