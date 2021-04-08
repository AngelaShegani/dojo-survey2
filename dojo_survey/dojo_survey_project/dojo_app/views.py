from django.shortcuts import render, redirect
def index(request):
    return render(request,'index.html')
def results(request):
    if request.method == "GET":
    	print(request.GET)
    if request.method == "POST":
        print(request.POST)
        request.session['first_name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['location']
        request.session['favorite_language'] = request.POST['language']
        request.session['dojo_comment'] = request.POST['comment']
        request.session['favorite_framework'] = request.POST['radio']
    return render(request,'results.html')

def index2(request):
    print('got here from redirect!')
    return redirect('/')

    
    
