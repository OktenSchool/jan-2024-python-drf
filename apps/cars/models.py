from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)

    brand = models.CharField(max_length=10, validators=(V.MinLengthValidator(2),))
    price = models.IntegerField(validators=(V.MinValueValidator(0), V.MaxValueValidator(1_000_000)))
    year = models.IntegerField(validators=(V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)))
    body_type = models.CharField(max_length=9, choices=BodyTypeChoices.choices, blank=False, null=False)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()
