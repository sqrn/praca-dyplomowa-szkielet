@csrf_protect
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    m = User.objects.get(username=user.username)

                    login(request, user)
                    request.session['user_id'] = m.id
                    return redirect("/")

                else:
                    messages.warning(request, 
			"Twoje konto zostało zablokowane.")
            else:
                messages.warning(request, 
			"Nie ma takiego użytkownika lub źle wprowadzone hasło.")
        else:
            messages.warning(request, 
			"Źle wypełniony formularz")
    else:
        messages.warning(request, 
			"Nie przesłano żadnych danych!")
    
    return render_to_response('start_page.html', {
        'form': form,
    },
    context_instance=RequestContext(request)
    )
