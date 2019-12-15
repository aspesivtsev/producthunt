from django.shortcuts import render

def test_account(request):
    return render(request, 'accounts.html')

