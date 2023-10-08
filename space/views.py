from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Moon
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    return render(request, 'space/main.html')

def moon(request):
    europa = Moon.objects.order_by('data_added')
    context = {'moon': moon}
    return render(request, 'space/moon.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'space/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('space:main')
        else:
            return render(request, 'space/main.html', {'error': 'Invalid username or password'})
    return render(request, 'space/main.html')

#Testing Logic - ***FOR DEVELOPMENT ONLY***
# def register_view(request):
#     if request.method == "POST":
#         data = json.loads(request.body.decode("utf-8"))
        
#         username = data.get("username")
#         password = data.get("password")
#         email = data.get("email")

#         if not username or not password or not email:
#             return JsonResponse({"error": "Missing required parameters"}, status=400)

  
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({"error": "Username already exists"}, status=400)

    
#         user = User(username=username, email=email)
#         user.set_password(password)
#         user.save()

#         return JsonResponse({"success": "User registered successfully"})

#     return JsonResponse({"error": "Invalid request method"}, status=405)