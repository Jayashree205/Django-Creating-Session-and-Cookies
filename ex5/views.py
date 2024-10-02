from django.shortcuts import render, redirect

def index(request):
    return render(request, 'ex5/index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        request.session['username'] = username
        return redirect('ex5:welcome')  # Use namespaced URL name if needed
    return render(request, 'login.html')

def welcome_view(request):
    username = request.session.get('username', 'Guest')
    return render(request, 'welcome.html', {'username': username})
