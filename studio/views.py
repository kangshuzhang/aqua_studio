from django.shortcuts import render
from studio.models import contamination
import numpy as np
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
import datetime
def home(request):
    page=render(request,'home.html')
    return page
def diary(request):
    today=datetime.date.today()
    date1=today+datetime.timedelta(days=-1)
    date2=today+datetime.timedelta(days=-2)
    date3=today+datetime.timedelta(days=-3)
    date4=today+datetime.timedelta(days=-4)
    date5=today+datetime.timedelta(days=-5)
    date6=today+datetime.timedelta(days=-6)
    contamination1=contamination.objects.get(date=date1)
    web_page=render(request,'diary.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6})
    return web_page
def diary2(request):
    today=datetime.date.today()
    delta = datetime.timedelta(days=-1)
    date=today+delta
    contamination1=contamination.objects.get(date=date)
    web_page=render(request,'diary2.html',{'contamination':contamination1,'date':date})
    return web_page
def diary3(request):
    today=datetime.date.today()
    delta = datetime.timedelta(days=-2)
    date=today+delta
    contamination1=contamination.objects.get(date=date)
    web_page=render(request,'diary3.html',{'contamination':contamination1,'date':date})
    return web_page
def diary4(request):
    today=datetime.date.today()
    delta = datetime.timedelta(days=-3)
    date=today+delta
    contamination=contamination.objects.get(date=date)
    web_page=render(request,'diary4.html',{'contamination':contamination,'date':date})
    return web_page
def diary5(request):
    today=datetime.date.today()
    delta = datetime.timedelta(days=-4)
    date=today+delta
    contamination=contamination.objects.get(date=date)
    web_page=render(request,'diary5.html',{'contamination':contamination,'date':date})
    return web_page
def diary6(request):
    today=datetime.date.today()
    delta = datetime.timedelta(days=-5)
    date=today+delta
    contamination=contamination.objects.get(date=date)
    web_page=render(request,'diary6.html',{'contamination':contamination,'date':date})
    return web_page
def diary7(request):
    today=datetime.date.today()
    delta = datetime.timedelta(days=-6)
    date=today+delta
    contamination=contamination.objects.get(date=date)
    web_page=render(request,'diary7.html',{'contamination':contamination,'date':date})
    return web_page
def data(request):
    a=np.arange(50)
    b=np.arange(50)
    TOOLS = "hover,crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select"
    picture = figure(width=800, height=400, tools=TOOLS)  
    picture.line(a, b, color='blue', alpha=0.5)
    script, div = components(picture, CDN)
    return render(request, 'data.html', {'script': script, 'div': div})
# Create your views here.
