from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    room_number = models.CharField(max_length=4)

    def __str__(self):
        return " ".join([self.first_name, self.last_name])

class ItemRequest(models.Model):
    item_name = models.CharField(max_length=70)
    time = models.DateTimeField()
    quantity = models.BigIntegerField()
    user_ID = models.CharField(max_length=70)


    def __str__(self):
        return str(self.quantity) + " " + str(self.item_name) + " ordered by user " + str(self.user_ID) + " at " + str(self.time)