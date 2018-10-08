from django.db import models
from django.contrib.auth.models import User
from PIL import Image #from pillow library

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cascade: on deleting User, it deletes Profile and on deleting Profile, it doesn't delete User
    bio = models.CharField(max_length=1000, blank=True)
    portfolio = models.URLField(blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    #Overriding the default save method to resize the picture uploaded
    def save(self):
        super().save() #running save() method of parent class through super()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
