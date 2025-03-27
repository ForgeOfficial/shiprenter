from django.db import models

from app.models.Size import Size
from app.models.Category import Category


class Ship(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ships')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="ships")
    crew = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    image = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        ordering = ['name']
