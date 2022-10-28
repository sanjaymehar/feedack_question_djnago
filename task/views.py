from django.shortcuts import render,redirect
from task.models import Question,sesion,Feedbacks
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    a=Question.objects.all()
    idd=[]
    for i in a:
        idd.append(str(i.id))

    request.session['allid']=idd
    request.session['current']=0

    return redirect(f'/h/{idd[request.session.get("current")]}')

def vote(request,pk):
    qs=Question.objects.get(id=pk)
    a=Question.objects.all()
    ques=[]
    for i in a:
        ques.append(str(i.id))

    print(ques,pk,"hello")
    if pk==ques[-1]:
        return render(request,'ques.html',{'questions':qs,"last":"last","total":len(ques),"index":ques.index(pk)+1})

    elif str(pk)==ques[0]:
       
        return render(request,'ques.html',{'fisrt':'fisrt','questions':qs,"total":len(ques),"index":ques.index(pk)+1})
    else:
        return render(request,'ques.html',{'questions':qs,"total":len(ques),"index":ques.index(pk)+1})

@csrf_exempt
def next(request):
 
    if request.method == "POST":
        se=sesion.objects.filter(sid=request.session.session_key).first()
        if not se:
            se=sesion.objects.create(sid=request.session.session_key)
            se.save()
            request.session['current']=0
        #x=request.session.get("allid")
        idd=request.session.get("allid")    
        qobj=Question.objects.get(id=idd[int(request.session.get("current"))])
        if 'dataa' in request.POST:
            fedobj=Feedbacks.objects.filter(sid=se,question=qobj).first()
            if fedobj:
                fedobj.text=request.POST['dataa']
                fedobj.save()
            else:
                Feedbacks.objects.create(sid=se,question=qobj,text=request.POST['dataa']).save()
        elif 'data' in request.POST:
            fedobj=Feedbacks.objects.filter(sid=se,question=qobj).first()
            if fedobj:
                fedobj.text=request.POST['data']
                fedobj.save()
            else:
                Feedbacks.objects.create(sid=se,question=qobj,text=request.POST['data']).save()
       
        request.session['current']+=1     
        x=request.session.get("current")

        if int(x)==len(idd):
            request.session.pop('allid')
            return render(request,"thankyou.html")
        else:
            return redirect(f'/h/{idd[request.session.get("current")]}')

      

    if request.method == "GET":
        idd=request.session.get("allid")
        qobj=idd[int(request.session.get("current"))]
        print(idd,qobj,"aaaaaaa")
        qobj=Question.objects.get(id=qobj)

        request.session['current']+=1     
        x=request.session.get("current")

        if int(x)==len(idd):
            request.session.pop('allid')
            return render(request,"thankyou.html")
        else:
            return redirect(f'/h/{idd[request.session.get("current")]}')

        


@csrf_exempt
def previous(request):
    if request.method == "GET":
        idd=request.session.get("allid")        
        x=idd[request.session.get("current")]
        if int(x)==1:         
            return redirect(f'/h/{idd[0]}')
        else:
            request.session['current']-=1
            return redirect(f'/h/{idd[request.session.get("current")]}')

def start(request):
    return render(request,'hello.html')
