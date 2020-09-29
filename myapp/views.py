from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Devotee
from myapp.forms import feedbackform
from . import forms

def page_count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    return render(request,'myapp/count.html',{'count':newcount})

def thankyou_view(request):
    if request.method=='POST':
        form=forms.feedbackform(request.POST)
        if form.is_valid():
            print('Form Validation success and printing feedback info')
            print('Devotee:',form.cleaned_data['name'])
            print('email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['Feedback'])
            sent=True
    form=feedbackform()
    return thankyou_view(request)
    return render(request,'myapp/thankyou.html',{'name':form.cleaned_data['name']})

def display_name(request):
    my_dict={'name':name,'feedback':feedback}
    return render(request,'myapp/thankyou.html',{'name':name,'feedback':feedback})
def home_page(request):
    return render(request,'myapp/home.html')
def pillay(request):
    return render(request,'myapp/pillay.html')

def chakra(request):
    return render(request,'myapp/chakra.html')
def dhumal(request):
    return render(request,'myapp/dhumal.html')

def udi(request):
    return render(request,'myapp/udi.html')

def saibaba(request):
    return render(request,'myapp/saibaba.html')

def hemadpant(request):
    return render(request,'myapp/hem.html')

def astakam(request):
    return render(request,'myapp/astakam.html')

def sathe(request):
    return render(request,'myapp/sathe.html')

def stavanamanjari(request):
    return render(request,'myapp/stavanamanjari.html')

def pradhan(request):
    return render(request,'myapp/pradhan.html')

def chalisa(request):
    return render(request,'myapp/chalisa.html')


def wpradhan(request):
    return render(request,'myapp/wpradhan.html')

def nagesh(request):
    return render(request,'myapp/nagesh.html')

def hansraj(request):
    return render(request,'myapp/hansraj.html')

def thukaram(request):
    return render(request,'myapp/thukaram.html')


def kolambo(request):
    return render(request,'myapp/kolambo.html')


def shankar(request):
    return render(request,'myapp/somnath.html')


def clerk(request):
    return render(request,'myapp/clerk.html')


def dev(request):
    return render(request,'myapp/dev.html')

def mulky(request):
    return render(request,'myapp/mulky.html')


def gangadhar(request):
    return render(request,'myapp/gangadhar.html')

def munge(request):
    return render(request,'myapp/munge.html')


def nanda(request):
    return render(request,'myapp/nandaram.html')

def bvdev(request):
    return render(request,'myapp/bvdev.html')

def sagun(request):
    return render(request,'myapp/sagun.html')


def dasaganu(request):
    return render(request,'myapp/dasaganu.html')

def kaka(request):
    return render(request,'myapp/kaka.html')

def kapar(request):
    return render(request,'myapp/kapar.html')


def anna(request):
    return render(request,'myapp/anna.html')

def appaji(request):
    return render(request,'myapp/appaji.html')


def jayker(request):
    return render(request,'myapp/jayker.html')


def bhate(request):
    return render(request,'myapp/bhate.html')

def mahadev(request):
    return render(request,'myapp/mahadev.html')


def rasane(request):
    return render(request,'myapp/rasane.html')


def kusha(request):
    return render(request,'myapp/kusha.html')

def damodar(request):
    return render(request,'myapp/damodar.html')


def tarabhai(request):
    return render(request,'myapp/tarabhai.html')

def appasaheb(request):
    return render(request,'myapp/appasaheb.html')


def raosahib(request):
    return render(request,'myapp/raosahib.html')

def nanasaheb(request):
    return render(request,'myapp/nanasaheb.html')

def bhagoji(request):
    return render(request,'myapp/bhagoji.html')

def keshav(request):
    return render(request,'myapp/keshav.html')

def nanac(request):
    return render(request,'myapp/nanac.html')


def booti(request):
    return render(request,'myapp/booti.html')




def arthi(request):
    return render(request,'myapp/arthi.html')


def abdulbaba(request):
    return render(request,'myapp/abdulbaba.html')


def badebaba(request):
    return render(request,'myapp/badebaba.html')

def lakshmi_bhai_shinde(request):
    return render(request,'myapp/lakshmi.html')

def answers(request):
    return render(request,'myapp/babaanswers.html')

def radha(request):
    return render(request,'myapp/radha.html')

def nana(request):
    return render(request,'myapp/nana.html')

def diyas(request):
    return render(request,'myapp/diyas.html')

def more(request):
    return render(request,'myapp/more.html')

def divya(request):
    return render(request,'myapp/divya.html')

def shiridi_page(request):
    return render(request,'myapp/page1.html')

def satcharitra_page(request):
    return render(request,'myapp/page5.html')

def archana(request):
    return render(request,'myapp/108.html')
def shiridi(request):
    return render(request,'myapp/page2.html')

def vrat(request):
    return render(request,'myapp/vrat.html')

def nava(request):
    return render(request,'myapp/nava.html')

def stotram(request):
    return render(request,'myapp/stotram.html')

def sidebar(request):
    return render(request,'myapp/page3.html')

def maha(request):
    return render(request,'myapp/maha.html')

def tatya(request):
    return render(request,'myapp/tatya.html')

def neem(request):
    return render(request,'myapp/neem.html')


def baijamai(request):
    return render(request,'myapp/bhaijamai.html')

def shyama(request):
    return render(request,'myapp/shyama.html')

def devoteeview(request):
    dev_list=Devotee.objects.all()
    my_dict={'dev_list':dev_list}
    return render(request,'myapp/devlist.html',context=my_dict)

def DevoteeRegisterview(request):
    form=forms.DevoteeRegister
    return render(request,'myapp/register.html',context={'form':form})

def feedbackview(request):
    #sent=False
    #form=forms.feedbackform()
    if request.method=="GET":
        form=forms.feedbackform()
        return render(request,'myapp/feedback.html',{'form':form})
    if request.method=='POST':
        form=forms.feedbackform(request.POST)
        if form.is_valid():
            print('Form Validation success and printing feedback info')
            print('Devotee:',form.cleaned_data['name'])
            print('email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['Feedback'])
            #sent=True
    form=feedbackform()
    return render(request,'myapp/input.html',{'form':form,})
