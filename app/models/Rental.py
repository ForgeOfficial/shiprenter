from django.db import models
from django.conf import settings

class Rental(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rentals'
    )
    ship = models.ForeignKey(
        'Ship',
        on_delete=models.CASCADE,
        related_name='rentals'
    )
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.ship.name} ({self.duration} jours)"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def total_price(self):
        return self.ship.price * self.duration