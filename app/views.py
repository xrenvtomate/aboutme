from django.shortcuts import render


cnt = 0

def index(req):
    global cnt
    cnt += 1
    return render(req, 'index.html', {"count": cnt})
