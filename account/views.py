from pyexpat.errors import messages

from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model, authenticate , login, logout
from .forms import SignUpForm
from django.contrib import messages

User = get_user_model()

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, "Bunday foydalanuvchi topilmadi , ro'yxatdan utmagan ")
            return render(request, 'account/login.html')
        login(request, user)
        messages.info(request, "Hush kelibsiz | Login successfull ! ")
        return redirect('product:home')
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Logout successfully ! ")
    return redirect('product:home')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request , "Siz muoffaqqiyatli ro'yxatdan o'tdingiz")
            return redirect('account:login')
        messages.warning(request , "Qayta urinib ko'ring ")

    form = SignUpForm()

    context = {'form': form}

    return render(request , 'account/register.html' , context)

def profile(request):
    user = User.objects.get(username=request.user , email=request.user.email)
    context = {'user': user}
    return render(request,  'account/profile.html' , context)










