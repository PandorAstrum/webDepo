from django.db import models

# Create your models here.

class test(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class bootstrap_Carousel(models.Model):
    name_alt = models.CharField(max_length=30)
    slider_title = models.CharField(max_length=30)
    slider_caption = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)
    slider_fading_type = models.CharField(max_length=100, null=True)
    data_slide_to = models.IntegerField(null=True)
    indicator_name = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name_alt

class owl_PhotoSlide(models.Model):
    name_alt = models.CharField(max_length=30)
    #image here
    image = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name_alt

class accordion1_content(models.Model):
    name = models.CharField(max_length=10)
    image = models.FileField(null=True)
    acc1_title = models.CharField(max_length=100)
    acc1_desc = models.CharField(max_length=200)
    acc1_content_link = models.URLField(max_length=1000, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class accordion2_content(models.Model):
    name = models.CharField(max_length=10)
    image = models.FileField(null=True)
    acc2_title = models.CharField(max_length=100)
    acc2_desc = models.CharField(max_length=300)
    acc2_content_link = models.URLField(max_length=1000, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class accordion3_content(models.Model):
    name = models.CharField(max_length=100)
    acc3_title = models.CharField(max_length=100)
    acc3_desc = models.CharField(max_length=400)
    acc3_content_link = models.URLField(max_length=1000, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class accordion4_content(models.Model):
    name = models.CharField(max_length=100)
    acc4_title = models.CharField(max_length=100)
    acc4_desc = models.CharField(max_length=400)
    acc4_content_link = models.URLField(max_length=1000, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name




















