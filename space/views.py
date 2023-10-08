from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Moon

# Create your views here.
def main(request):
    return render(request, 'space/main.html')

def moon(request):
    europa = Moon.objects.order_by('data_added')
    context = {'moon': moon}
    return render(request, 'space/moon.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'space/register.html', {'form': form})