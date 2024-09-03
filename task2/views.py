from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def func_template(request):
    return render(request, 'func_template.html')