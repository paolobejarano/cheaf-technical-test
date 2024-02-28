import datetime

from django.core.validators import MinValueValidator
from django.db import models

from main.models.time_stamp import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    expires_at = models.DateField(db_index=True)

    def __str__(self):
        return self.name

    def create_alert(self, days_before: int):
        from main.models.alert import Alert
        alert = Alert()
        alert.product = self
        alert.days_before = days_before
        return alert

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """Override save method to create two alerts when a product is created."""
        is_created = self._state.adding
        if is_created:
            alert_1 = self.create_alert(10)
            alert_2 = self.create_alert(5)
        super().save(force_insert, force_update, *args, **kwargs)
        if is_created:
            alert_1.save()
            alert_2.save()
