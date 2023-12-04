from django.db import models

# Create your models here.
class Destination(models.Model):
    image = models.ImageField(upload_to='media')
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    price_before = models.FloatField(default=0.0)
    itinerary = models.TextField(default='Default Itinerary') 


    def __str__(self):
        return self.location
    
    @property
    def imageURL(self):
            try:
                url = self.image.url
            except:
                url = ''
            return url
    

class Popular(models.Model):
    image = models.ImageField(upload_to='media')
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    price_before = models.FloatField(default=0.0)
    itinerary = models.TextField(default='Default Itinerary') 


    def __str__(self):
        return self.location
    
    @property
    def imageURL4(self):
            try:
                url = self.image.url
            except:
                url = ''
            return url

class Gallery(models.Model):
    image = models.ImageField(upload_to='media')
    destination = models.CharField(max_length=50)
    experience = models.CharField(max_length=500)

    def __str__(self):
        return self.experience
    
    @property
    def imageURL2(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Review(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.comment
    
    @property
    def imageURL3(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question
    





