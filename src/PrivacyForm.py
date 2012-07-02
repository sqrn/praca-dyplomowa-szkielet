class PrivacyForm(forms.ModelForm):
    email_priv = forms.CharField(
        label="E-mail", 
        widget=forms.Select(choices=PRIVACY),
        help_text="Kto widzi Twój adres e-mail")
    address_priv = forms.CharField(
        label="Miejsce zameldowania", 
        widget=forms.Select(choices=PRIVACY),
        help_text="Kto widzi Twój adres")
    inf_priv = forms.CharField(
        label="Informacje", 
        widget=forms.Select(choices=PRIVACY),
        help_text="Kto widzi informacje o Tobie")
    gender_priv = forms.CharField(
        label="Płeć", 
        widget=forms.Select(choices=PRIVACY),
        help_text="Kto widzi Twoją płeć")
    wall_priv = forms.CharField(
        label="E-mail", 
        widget=forms.Select(choices=PRIVACY),
        help_text="Kto widzi Twoją tablicę")

    def __init__(self, user, *args, **kwargs):
        super(PrivacyForm, self).__init__(*args, **kwargs)
        user_profile = get_user_profile(user)

        self.fields['email_priv'].initial= user_profile.privacy.email_priv
        self.fields['address_priv'].initial= user_profile.privacy.address_priv
        self.fields['inf_priv'].initial= user_profile.privacy.inf_priv
        self.fields['gender_priv'].initial= user_profile.privacy.gender_priv
        self.fields['wall_priv'].initial= user_profile.privacy.wall_priv

    class Meta:
        model = UserPrivacy
        exclude = ('user') 
