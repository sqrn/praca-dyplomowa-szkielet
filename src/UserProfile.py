class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    gender = models.CharField(
        max_length=10, 
        blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, 
        null=True, default=0)
    longtitude = models.DecimalField(
        max_digits=9, decimal_places=6, 
        null=True, default=0)
    friends = models.ManyToManyField(
        User, blank=True, 
        related_name="friends")
    address = models.CharField(
        max_length=255, null=True, 
        default='')
    privacy = models.ForeignKey('UserPrivacy')
    information = models.TextField(
        blank=True,default="")

    class Meta:
        verbose_name = "Profile użytkowników"
        verbose_name_plural = "Profile użytkowników"

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username

    def getLatitude(self):
        return (u'%.6f' % self.latitude)
    def getLongtitude(self):
        return (u'%.6f' % self.longtitude)

    def getLngLat(self):
        return (u'%.6f,%.6f' % (self.latitude, self.longtitude))

    def isFriend(self, friend_id):
        friends = self.friends.all()
        for i in friends:
            if i.id == friend_id:
                return True
        return False

    def addNewFriend(self, friend_id):
        """Dodaje nowa znajomosc o podanym ID "friend_id"""
        self.friends.add(friend_id)

    def get_absolute_url(self):
        return "/people/%i/" % self.user.id    
        
    def get_full_name(self):
        return "%s %s" % (
            self.user.first_name, 
            self.user.last_name
        )        
    def get_avatar_url(self):
        return "/media/accounts/%i/avatar.jpg" % self.user.id

def get_user_profile(user):
    return UserProfile.objects.get(user__exact=user)

