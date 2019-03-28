from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'main/base.html', {})



from django.contrib.auth import logout, authenticate, login



def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("/login/")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "registration/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "registration/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return login_request(request)


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_request(request):
    if request.user.is_authenticated:
        return render(request, 'chat/chatwindow.html', {});
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/login/")
                #return HttpResponseRedirect(reverse('/my_redirect/'))

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})
