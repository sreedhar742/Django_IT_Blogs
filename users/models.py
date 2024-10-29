from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='pic4.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# import io

# def get_default_image_data():
#     # Load the default image and convert it to byte data
#     with open('media/pic4.jpg', 'rb') as img_file:
#         return img_file.read()

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image_data = models.BinaryField(null=True, blank=True, default=get_default_image_data)

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         # If no image data is provided, use the default image
#         if not self.image_data:
#             self.image_data = get_default_image_data()

#         # Open the image from the binary data, resize, and save back to binary
#         img = Image.open(io.BytesIO(self.image_data))

#         # Check if the image exceeds the 300x300 limit
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)

#             # Save the resized image back to byte data
#             byte_arr = io.BytesIO()
#             img.save(byte_arr, format='PNG')  # Save format depends on your needs, e.g., 'JPEG' or 'PNG'
#             self.image_data = byte_arr.getvalue()

#         super().save(*args, **kwargs)
