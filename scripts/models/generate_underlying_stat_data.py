from django.core.exceptions import ValidationError
from django.db import models

from commons.models import BaseModel


def _validate_ids(ids):
    ids = ids.replace(" ", "")
    ids = ids.strip(",")
    id_list = ids.split(",")
    for id in id_list:
        try:
            int(id)
        except ValueError:
            raise ValidationError("Id is not an integer")


class GenerateUnderlyingStatData(BaseModel):
    ids = models.TextField(validators=[_validate_ids])

    def save(self):
        self.ids = self.ids.replace(" ", "")
        self.ids = self.ids.strip(",")
        return super().save()

    class Meta:
        verbose_name_plural = "Generate underlying stat data"
