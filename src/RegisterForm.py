class RegisterForm(forms.Form):
    username = forms.CharField(label=(u'Użytkownik'))
    email = forms.EmailField(label=(u'Adres e-mail'))
    password = forms.CharField(label=(u'Hasło'),
        widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label=(u'Hasło ponownie'),
        widget=forms.PasswordInput(render_value=False))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user_ipaddr = None

    def save(self,):
        username = self.cleaned_data['username'].lower()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        
        username = username.split()

        email_test = User.objects.filter(email=email)
        username_test = User.objects.filter(username=username[0])
        msg = []

        if len(username) > 1:
            msg.append("Nazwa nie może zawierać znaków specjalnych w tym spacji.")

        # jezeli konto z podanym username istenieje w bazie
        elif username_test.count() > 0:

            msg.append("Podana nazwa użytkownika istnieje.")

        elif email_test.count() > 0:
            msg.append("Konto istnieje.")
        
        elif password != password2:
            msg.append("Hasła muszą być takie same.")

        if len(msg) > 0:
            msg.append("error")
            return msg
        else:
            username = username[0]
            user = User.objects.create_user(
                username, 
                email,
                password
            )
            user.is_staff = False


            ## tworzenie nowego profilu dla uzytkownika
            users_profile = UserProfile()
            users_profile.user_id = user.id

            # tworzenie prywatnosci
            users_profile.privacy = self.createPrivacy(user)

            ## ustalanie adresu IP przybywajacego
            g = GeoIP(settings.GEOPATH)
            print self.user_ipaddr
            try: 
                city = g.city(self.user_ipaddr)['city']
                lat, lon = g.lat_lon()
            except Exception:
                city = ""
                lat, lon = (0,0)

            users_profile.address = city
            users_profile.latitude = lat
            users_profile.longtitude = lon
            users_profile.save()

            ## jezeli user zostal utworzony, utworz katalogi
            try:
                self.__mkdir(user.id)
                # jezeli wszystko przebieglo pomyslnie
                msg.append("Utworzono nowe konto.")
                msg.append("success")
            except Exception, m:
                msg.append(m)
                msg.append("error")

            return msg
    def save_ip(self, user_ipaddr):
        self.user_ipaddr = user_ipaddr

    def __mkdir(self, user_id):
        ## tworzenie katalogow dla nowego usera
        path = '%s/accounts/%s' % (settings.MEDIA_ROOT, user_id)
        try:
            os.mkdir(path,0770)
        except OSError:
            raise Exception("Wystąpił nieoczekiwany błąd systemu. Spróbuj ponownie.")
        except IOError:
            raise Exception("Wystąpił nieoczekiwany błąd. Spróbuj ponownie.")
            
        command = "cp %saccounts/none.jpg %s/accounts/%s/avatar.jpg" % (
            settings.MEDIA_ROOT, 
            settings.MEDIA_ROOT, 
            user_id
        )
        try:
            os.system(command)
        except os.error:
            raise Exception("Wystąpił nieoczekiwany błąd. Spróbuj ponownie.")

    def createPrivacy(self, user):
        try:
            privacy = UserPrivacy()
            privacy.user = user
            privacy.save()
        except Exception:
            return None
        return privacy
