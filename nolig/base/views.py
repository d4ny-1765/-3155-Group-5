from django.shortcuts import render
# Create your views here.



def home(request):
    context ={}
    return render(request, 'home.html')

def discussion(request):
    return render(request, 'discussion.html')

