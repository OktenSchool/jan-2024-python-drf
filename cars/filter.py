from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from cars.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case _:
                raise ValidationError(f"Filter {k} not supported")
    return qs
