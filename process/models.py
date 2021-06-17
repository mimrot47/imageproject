from django.db import models
from .utils import get_filtered_images
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from PIL import Image
from PIL.ExifTags import TAGS

# Create your models here.
ACTION_CHOICE=(
    ('NO_FILTER','NO_FILTER'),
    ('HISTOGRAM','HISTOGRAM'),
    ('COLORIZE','COLORIZE'),
    ('GRAYSCALE','GRAYSCALE'),
    ('HSV','HSV CONVERGEN'),
    ('BLURRED','BLURRED'),
    ('BINARY','BINARY'),
    ('INVERT','BINARY INVERS'),
    ('EADGES','EADGES DETECTION'),
    ('NOICE','REDUCE NOICE')
)
class Uplod(models.Model):
    image=models.ImageField(upload_to='images')
    action=models.CharField(max_length=50,choices=ACTION_CHOICE,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.id)
    


        
    def save(self,*args,**kwargs):
        pil_img=Image.open(self.image)
        exifdata = pil_img.getexif()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data1 = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:60}: {data1}")
        cv_img=np.array(pil_img)
        img=get_filtered_images(cv_img,self.action)
        im_pil=Image.fromarray(img)
        buffer=BytesIO()
        im_pil.save(buffer,format='png')
        image_png=buffer.getvalue()
        self.image.save(str(self.image),ContentFile(image_png),save=False)
        super().save(*args, **kwargs)


