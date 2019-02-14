from django.db import models

class Tweet(models.Model):
    tweet = models.Textfield()
    update = models.datetimefield(auto_now = True)

