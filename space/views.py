from django.shortcuts import render
from .models import Moon

# Create your views here.
def main(request):
    return render(request, 'space/main.html')

def moon(request):
    europa = Moon.objects.order_by('data_added')
    context = {'moon': moon}
    return render(request, 'space/moon.html', context)