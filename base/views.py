from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/home.html')

def your_view(request):
    context = {
        'your_email': 'your@email.com',
    }
    return render(request, 'your_template.html', context)