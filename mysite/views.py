from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys,datetime

def hello(request):
    Path = sys.path
    return HttpResponse("<h1>Hello world</h1>" + "<code>" + str(Path)+"</code>")
def index(request):
    # Path = sys.path
    # return HttpResponse("<html><p>Welcome to Pi!</p></html>")
    # now = datetime.datetime.now()
    lists = ['Michael', 'Bob', 'Tracy']
    return render_to_response('index.html',{'lists':lists})
    # return render_to_response('index.html', [1,2,3,4])
def time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def offset(request,num,charset):
    now = datetime.datetime.now()
    html = "<html><body>the num is :" +num + " charset is:"+charset +"</body></html>"
    return HttpResponse(html)