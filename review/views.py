from django.shortcuts import render

def my_view(request):
    my_variable = "Hello, World!"
    return render(request, 'review/index.html', {'my_variable': my_variable})
