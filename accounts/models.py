from django.db import models

from django.conf import settings


class UserProfileManager(models.Manager):
    use_for_related_fields = True
    def all(self):
        qs= self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

    def toggle_follow(self, user, to_toggle_user):

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(toggle_user)
            added = False
        else:
            user_profile.following.add(to_toggle_user) 
            added = True
        return added    


    def is_following(self, user, followed_by_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False

class UserProfile(models.Model):
    user      = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete =  models.CASCADE, related_name = "profile")
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,  blank=True, related_name = "followed_by")
    
    objects = UserProfileManager() #userprofile.objects.all()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def get_follow_by(self):
        users = self.follow_by.all()
        return users.exclude(username=self.user.username)