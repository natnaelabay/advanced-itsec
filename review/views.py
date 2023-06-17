from django.shortcuts import render
from review.forms import FeedbackForm

def my_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'review/add.html')
    else:
        form = FeedbackForm()
    return render(request, 'review/add.html', {'form': form})