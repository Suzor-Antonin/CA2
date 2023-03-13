from django.db import models
from django.urls import reverse


class Building(models.Model):
    name = models.CharField(max_length=50, default='Dorset College')
    floors = models.PositiveSmallIntegerField(default=1)
    color = models.CharField(max_length=50, default='Brick Red')
    residential = models.BooleanField(default=True)

    country = models.CharField(max_length=20, default='Ireland')
    city = models.CharField(max_length=20, default='Dublin')
    street = models.CharField(max_length=100, default='Belvedere Place, Mountjoy Square')
    number = models.CharField(max_length=10, default='7 & 8')

    def __str__(self):
        # return ', '. join([self.name, self.number, self.street, self.city, self.country])
        return self.name + ' (' + self.get_address1() + ')'

    def get_absolute_url(self):
        return reverse('buildings:read', kwargs={'pk': self.pk})

    def get_address1(self):
        return ', '.join([self.number, self.street, self.city, self.country])

    def get_address2(self):
        return ', '.join([self.country, self.city, self.street, self.number])
