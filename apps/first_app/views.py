from django.shortcuts import render, redirect, HttpResponse
import time
from time import gmtime, strftime


# Create your views here.
def index(request):
    
    if 'word' not in request.session:
        request.session['word'] = ''
    if 'color' not in request.session:
        request.session['color'] = ''
    if 'full_string' not in request.session:
        request.session['full_string'] = []
    if 'font_size' not in request.session:
        request.session['font_size'] = 'font_size'
    context = {
        'newword': request.session['full_string'],
    }
    return render(request, "first_app/index.html", context)

def process(request):
    timestamp = '<span style="display: inline-block:">--added on' + strftime('%B %d %I:%M')+'</span>'
    if request.method == "POST":
        print(time)
        request.session['word'] =  request.POST['word']
        request.session['color'] = request.POST['color']
        if request.session['color'] == 'red' and 'font_size' in request.POST:
            word = "<p class='redbig'>" + request.session['word'] + "</p>" 
        if request.session['color'] == 'blue' and 'font_size' in request.POST:
            word = "<p class='bluebig'>" + request.session['word'] + "</p>"
        if request.session['color'] == 'green' and 'font_size' in request.POST:
            word = "<p class='greenbig'>" + request.session['word'] + "</p>"

        if request.session['color'] == 'red' and 'font_size' not in request.POST:
            word = "<p class='red'>" + request.session['word'] + "</p>"
        if request.session['color'] == 'blue' and 'font_size' not in request.POST:
            word = "<p class='blue'>" + request.session['word'] + "</p>"
        if request.session['color'] == 'green' and 'font_size' not in request.POST:
            word = "<p class='green'>" + request.session['word'] + "</p>"
        request.session['full_string'].append(word + timestamp)
    return redirect('/')
def reset(request):
    request.session.clear()
    return redirect('/')    


    # string = ''
    # if request.method == "POST":
    #     request.session['full_str'] = []
    #     request.session['word'] = request.POST['word']
    #     # print(request.session['word'])    
    #     request.session['color'] = request.POST['color']
    #     # request.session['big'] = request.POST['big']
    #     print(request.session['new_word'])
    #     strings = "<p style='color: red;'>"+ request.session['word'] +"</p>"
    #     request.session['full_str'] += "<p style='color: red;'>"+ request.session['word'] +"</p>"
    #     request.session['full_str'].append(string)
    #     print(request.session['full_str']) 