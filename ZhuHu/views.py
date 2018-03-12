from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone
from django.template import RequestContext
from ZhuHu.models import User, Question


def signin(request):
    if request.method == 'POST':
        input_phone = request.POST['account']
        input_password = request.POST['password']
        # 查看是否有用户
        user = User.objects.filter(
            phone=input_phone,
            password=input_password,
        )
        if len(user) == 0:
            return HttpResponse('mistake input')
        else:
            return redirect('/people/'+str(+user[0].id))
    elif request.method == 'GET':

        # 这个地方要用 .GET.get() ,确保没有参数也能登入
        input_password = request.GET.get('password', '')
        input_name = request.GET.get('fullname', '')
        input_phone = request.GET.get('account', '')

        # filter得到的不是None，通过长度判断
        if input_password != '' and input_name != '' and len(User.objects.filter(name=input_name)) == 0:
            add = User()
            add.name = input_name
            add.password = input_password
            add.phone = input_phone
            add.save()
           # return redirect('http://127:0.0.1:8000/people/'+str(add.id))
        return render(request, 'home.html')


def people(request, user_id):
    user = User.objects.get(id=user_id)
    ctx = {
        'user': user,
        'user_questions': user.question_set.all()
    }
    #return HttpResponse('mistake input')
    if request.method == 'POST':

        input_title = request.POST.get('title', '')
        input_content = request.POST.get('content', '')
        if input_content != '' and input_content != '':
            add = Question()
            add.user = user
            add.title = input_title
            add.content = input_content
            add.release_date = timezone.now()
            add.save()
        return render(request, 'people.html', ctx)
    else:
        return render(request, 'people.html', ctx)

