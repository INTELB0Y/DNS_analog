from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=120)
    # about = models.CharField(max_length=120)
    price = models.IntegerField()
    # # haracteristic = models.CharField(max_length=200
    # # creator = models.CharField(max_length=200)
    # is_done = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to='images', default='/blank.jpg')

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.about


class Create(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)


# class/
