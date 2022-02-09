from commons.models import BaseModel
from django.db import models

class Kit(BaseModel):
    url = models.URLField(blank=False, null=False)
    name = models.CharField(blank=False,null=False, max_length=32)

