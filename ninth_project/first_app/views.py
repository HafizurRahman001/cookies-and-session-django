from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
def set_cookies(request):
    response = render(request,'home.html')
    # response.set_cookie('name','hafiz', max_age=30)
    response.set_cookie('name','hafiz', expires=datetime.utcnow() + timedelta(days= 7))
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})


def delete_cookie(request):
    response = render(request, 'delete.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name':'hafiz',
        'age': 22,
        'language':'Bengal'
    }
    request.session.update(data)
    return render(request,'home.html')


def get_session(request):
    if 'name' in request.session:
        data = request.session
        request.session.modified = True
        print(request.session['name'])
        return render(request,'session.html',{'data':data})
    else:
        return HttpResponse('Your session has been expired')





def delete_session(request):
    # del request.session['name'] # single data delete
    request.session.flush()
    return render(request,'delete.html')