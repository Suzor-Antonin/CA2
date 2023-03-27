from django.db import models
from django.urls import reverse
# The validator is used to control the `floors` value.
from django.core.validators import MinValueValidator


class Building(models.Model):
    name = models.CharField(max_length=50, default='Dorset College')
    # The `MinValueValidator` serves for the CreateView and UpdateView.
    # If the user enters a value of 0, the form will not post, and a notification will pop,
    # telling them that they must enter a value higher than or equal to 1.
    floors = models.PositiveSmallIntegerField(default=4, validators=[MinValueValidator(1)])
    color = models.CharField(max_length=50, default='Brick Red')
    residential = models.BooleanField(default=True)

    country = models.CharField(max_length=20, default='Ireland')
    city = models.CharField(max_length=20, default='Dublin')
    street = models.CharField(max_length=100, default='Belvedere Place, Mountjoy Square')
    number = models.CharField(max_length=10, default='7 & 8')

    # When a Building is created, we ensure that its `floors` value cannot be less than 1.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.floors < 1:
            self.floors = 1

    # When we make use of a shell, this will be printed to designate the Building object.
    def __str__(self):
        return self.name + ' (' + self.get_address1() + '), at pk: ' + str(self.pk)

    def get_absolute_url(self):
        return reverse('buildings:read', kwargs={'pk': self.pk})

    def get_address1(self):
        return ', '.join([self.number, self.street, self.city, self.country])

    def get_address2(self):
        return ', '.join([self.country, self.city, self.street, self.number])
