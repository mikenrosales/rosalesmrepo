from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.
def index(request):
    return HttpResponse('Mikole Rosales BSIT-3')

class IndexView(View):
    def get(self, request):
        return render(request, 'index.php', {})
