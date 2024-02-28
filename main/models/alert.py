import datetime

from django.core.validators import MinValueValidator
from django.db import models

from main.models.time_stamp import TimeStampedModel


class Alert(TimeStampedModel):
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, db_index=True, related_name='alerts')
    days_before = models.IntegerField(validators=[MinValueValidator(0)])

    @property
    def alert_at(self):
        """Return the date when the alert becomes active."""
        return self.product.expires_at - datetime.timedelta(days=self.days_before)

    @property
    def active(self) -> bool:
        """Return True if the alert is active, False otherwise.
        An alert is active if the product expires in more than days_before days."""
        return self.product.expires_at - datetime.timedelta(days=self.days_before) > self.created_at.date()

    @property
    def expired(self) -> bool:
        """Return True if the alert is expired, False otherwise.
        An alert is expired if the product expires in less than days_before days."""
        return self.product.expires_at - datetime.timedelta(days=self.days_before) < self.created_at.date()

    @property
    def days_until_activation(self) -> int:
        """Return the number of days before the alert becomes active. If number of days is negative, return 0.
        """
        return max((self.product.expires_at - datetime.timedelta(self.days_before) - datetime.date.today()).days, 0)

    @property
    def days_since_activation(self) -> int:
        """Return the number of days since the alert became active. If number of days is negative, return 0."""
        return max((datetime.date.today() - self.product.expires_at + datetime.timedelta(self.days_before)).days, 0)