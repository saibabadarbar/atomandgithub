"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
#from myapp import views
from django.conf.urls.static import static
#from blogapp import views
import myapp.views
#import blogapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('list/',blogapp.views.post_list_view),
    #re_path('^(?P<id>\d+)/share', blogapp.views.mail_send_view),
    #re_path('^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',blogapp.views.post_detail_view),
    path('udi/',myapp.views.udi),
    path('astakam/',myapp.views.astakam),
    path('hemadpant/',myapp.views.hemadpant),
    path('sagun/',myapp.views.sagun),
    path('stavanamanjari/',myapp.views.stavanamanjari),
    path('dhumal/',myapp.views.dhumal),
    path('chalisa/',myapp.views.chalisa),
    path('saibaba/',myapp.views.saibaba),
    path('sathe/',myapp.views.sathe),
    path('pradhan/',myapp.views.pradhan),
    path('wpradhan/',myapp.views.wpradhan),
    path('chakra/',myapp.views.chakra),
    path('thukaram/',myapp.views.thukaram),
    path('kolambo/',myapp.views.kolambo),
    path('shankar/',myapp.views.shankar),
    path('clerk/',myapp.views.clerk),
    path('hansraj/',myapp.views.hansraj),
    path('nagesh/',myapp.views.nagesh),
    path('mulky/',myapp.views.mulky),
    path('dev/',myapp.views.dev),
    path('gangadhar/',myapp.views.gangadhar),
    path('munge/',myapp.views.munge),
    path('nanda/',myapp.views.nanda),
    path('bvdev/',myapp.views.bvdev),
    path('kaka/',myapp.views.kaka),
    path('home/',myapp.views.home_page),
    path('dasaganu/',myapp.views.dasaganu),
    path('page1/',myapp.views.shiridi_page),
    path('booti/',myapp.views.booti),
    path('kusha/',myapp.views.kusha),
    path('rasane/',myapp.views.rasane),
    path('damodar/',myapp.views.damodar),
    path('nanasaheb/',myapp.views.nanasaheb),
    path('appasaheb/',myapp.views.appasaheb),
    path('keshav/',myapp.views.keshav),
    path('tarabhai/',myapp.views.tarabhai),
    path('appaji/',myapp.views.appaji),
    path('raosahib/',myapp.views.raosahib),
    path('bhagoji/',myapp.views.bhagoji),
    path('pillay/',myapp.views.pillay),
    path('mahadev/',myapp.views.mahadev),
    path('bhate/',myapp.views.bhate),
    path('anna/',myapp.views.anna),
    path('kapar/',myapp.views.kapar),
    path('jayker/',myapp.views.jayker),
    path('page5/',myapp.views.satcharitra_page),
    path('lakshmi_bhai_shinde/',myapp.views.lakshmi_bhai_shinde),
    path('page3/',myapp.views.sidebar),
    path('abdulbaba/',myapp.views.abdulbaba),
    path('arthi/',myapp.views.arthi),
    path('mahalsapathi/',myapp.views.maha),
    path('answers/',myapp.views.answers),
    path('badebaba/',myapp.views.badebaba),
    path('nanac/',myapp.views.nanac),
    path('radha/',myapp.views.radha),
    path('nana/',myapp.views.nana),
    path('more/',myapp.views.more),
    path('tatya/',myapp.views.tatya),
    path('baijamai/',myapp.views.baijamai),
    path('shyama/',myapp.views.shyama),
    path('neem/',myapp.views.neem),
    path('divya/',myapp.views.divya),
    path('diyas/',myapp.views.diyas),
    path('vrat/',myapp.views.vrat),
    path('count/',myapp.views.page_count_view),
    path('shiridi/',myapp.views.shiridi),
    path('nava/',myapp.views.nava),
    path('stotram/',myapp.views.stotram),
    path('archana/',myapp.views.archana),
    path('devlist/',myapp.views.devoteeview),
    path('register/',myapp.views.DevoteeRegisterview),
    path('feedback/',myapp.views.feedbackview),
    path('thankyou/',myapp.views.thankyou_view),
    path('input/',myapp.views.feedbackview),

]
