from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.shortcuts import reverse
from django.utils import timezone

PLAN_CHOICES = {
    ('N','No Active Plans'),
    ('M','Monthly Plan'),
    ('H','6 Months Plan'),
    ('Y','Yearly Plan')
}


# Create your models here.
class Movie(models.Model):  
    name = models.CharField(max_length=30)  
    genre = models.CharField(max_length=30)
    file = models.FileField()
    thumbnail = models.FileField()
    views = models.IntegerField()
    imdb = models.FloatField(null=True,blank=True)
    director = models.CharField(null=True,blank=True, max_length=50)
    actors =  models.CharField(null=True,blank=True , max_length=100)
    year = models.IntegerField(null=True,blank=True)
    prime_show = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('screens:movie_detail', args=[str(self.id)])



class Comment(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Plans(models.Model):
    plan_type = models.CharField(choices=PLAN_CHOICES,default='N',blank=True, null=True,max_length=2)
    plan_price = models.IntegerField(default=0)
    plan_length = models.IntegerField(default=0)

    def __str__(self):
        return self.plan_type

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE, blank=True, null=True)
    is_active_plan = models.BooleanField(default=False)
    plan_buy_date = models.DateTimeField(auto_now=False,null=True,blank=True)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="show_media/")
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user is None:
            print("Ther is not user found!")
            return "User Not found"
        return self.user.username

def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

def get_absolute_url(self):
    return reverse('screens:movie_detail', args=[str(self.id)])

