from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    usuario = User.objects.all()
    return render(request, 'Core/home.html', {
        "usuarios": usuario
    })
def corto(request):
    return render(request, 'Core/corto.html')
def bootstrap_builder(request):
    return render(request, 'Core/bootstrap_builder.html')
def contact(request):
    return render(request, 'Core/contact.html')
def admin(request):
    return render(request, 'Core/admin.html')
def business(request):
    return render(request, 'Core/business.html')
def education(request):
    return render(request, 'Core/education.html')
def portfolio(request):
    return render(request, 'Core/Portfolio.html')
def portfolio_builder(request):
    return render(request, 'Core/portfolio_builder.html')
def license(request):
    return render(request, 'Core/license.html')
def templates(request):
    return render(request, 'Core/templates.html')
def premium(request):
    return render(request, 'Core/premium.html')
def registro(request):
    if request.method == 'POST':
        usuario = request.POST['fullName']
        correo = request.POST['email']
        contrasena = request.POST['password']
        confirmar = request.POST['confirmPassword']
        if contrasena != confirmar:
            return render(request, "Core/CrearUsuario.html", {
                "error": "LA CONTRASEÑA NO ES LA CORRECTA"
            })
        if User.objects.filter(username=usuario).exists() & User.objects.filter(
                email=correo).exists() & User.objects.filter(username=usuario).exists():
            return render(
                request,
                "Core/CrearUsuario.html",
                {
                    "error": "Ese usuario ya existe."
                }
            )
        else:
            User.objects.create_user(

                username=usuario,
                email=correo,
                password=contrasena

            )

        return redirect("members")
    return render(request, 'Core/CrearUsuario.html')
def log_in(request):
    if request.method == 'POST':
        usuario = request.POST['email']
        contrasena = request.POST['password']
        user = authenticate(request, username=usuario, password=contrasena )
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "Core/members.html", {
                "error":"EL CORREO O LA CONTRASEÑA SON INCORRECTAS O NO EXISTEN"
            })
    return render(request, "Core/members.html")
def log_out(request):
    logout(request)
    return redirect("home")