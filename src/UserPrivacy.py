PRIVACY = (
    ('A', 'Wszyscy'),
    ('F', 'Tylko znajomi'),
    ('N', 'Tylko ja'),
)
class UserPrivacy(models.Model):
    user = models.ForeignKey(
        User, unique=True)
    email_priv = models.CharField(
        max_length=1, choices=PRIVACY, 
        default='F')
    address_priv = models.CharField(
        max_length=1, choices=PRIVACY, 
        default='A')
    inf_priv = models.CharField(
        max_length=1, choices=PRIVACY, 
        default='A')
    gender_priv = models.CharField(
        max_length=1, choices=PRIVACY, 
        default='A')
    wall_priv = models.CharField(
        max_length=1, choices=PRIVACY, 
        default='A')
        
    class Meta:
        verbose_name='Prywatność użytkowników'
        verbose_name_plural = "Prywatność użytkowników"
