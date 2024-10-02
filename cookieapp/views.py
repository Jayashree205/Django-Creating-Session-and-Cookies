from django.shortcuts import render, redirect

def index(request):
    return render(request, 'cookieapp/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mobile_number = request.POST.get('mobile_number')
        request.session['username'] = username
        response = redirect('welcome_view')  # Use namespaced URL name if needed
        response.set_cookie('username', username)
        return response
    return render(request, 'login1.html')

def welcome_view(request):
    username = request.session.get('username', 'Guest')
    username_cookie = request.COOKIES.get('username', 'Guest')
    return render(request, 'welcome1.html', {
        'username': username,
        'cookie_username': username_cookie
    })
