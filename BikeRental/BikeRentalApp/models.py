from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00

# Create your models here.
class Bike(models.Model):
    STANDARD = 'ST' 
    TANDEM = 'TA'
    ELECTRIC = 'EL'
    BYKE_TYPE_CHOICES = [
        ('STANDARD', 'Standard'),
        ('TANDEM', 'Tandem'),
        ('ELECTRIC', 'Electric')
    ]
    bike_type = models.CharField(max_length=8, choices=BYKE_TYPE_CHOICES, default='STANDARD')
    color = models.CharField(max_length=10, default='')

    def __str__(self) -> str:
        return self.bike_type + ' ' + self.color 

class Renter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    vip_num = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name + '-' + self.phone

class Rental(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.date.today)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f'Rental for {self.renter} of {self.bike} on {self.date}'
    
    def calc_price(self):
        curr_price = BASE_PRICE

        if self.bike.bike_type is 'TA':
            curr_price += TANDEM_SURCHARGE
        elif self.bike.bike_type is 'EL':
            curr_price += ELECTRIC_SURCHARGE
        elif self.renter.vip_num > 0:
            curr_price *= 0.8
        
        self.price = curr_price
