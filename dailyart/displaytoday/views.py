from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_view(request):
    """
    Handles a request to view the home page through the user's account
    """
    return render(request, 'displaytoday/home.html')
