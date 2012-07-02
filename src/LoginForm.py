class LoginForm(forms.Form):
    email = forms.EmailField(label=(u'Adres e-mail'))
    password = forms.CharField(label=(u'Hasło'),
        widget=forms.PasswordInput(render_value=False))
