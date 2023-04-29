from django.shortcuts import render, redirect
from .forms import RegisterForm
from CollectAll.models import SiteUser


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			uname = form.cleaned_data['username']
			form.save()
			user = SiteUser.objects.get(username=uname)
			user.save()
			return redirect('login')
		return redirect("index")
	else:
		form = RegisterForm()
	return render(request, 'register.html', {"form": form})
