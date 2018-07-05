from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from studio.models import contamination
import numpy as np
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select
from bokeh.embed import server_session
from bokeh.client import pull_session
from bokeh.layouts import gridplot
import datetime
import pandas as pd
from django_pandas.io import read_frame
import numpy as np
from collections import OrderedDict
from math import log, sqrt
import pandas as pd
from six.moves import cStringIO as StringIO
from pyecharts import Gauge, Line, Liquid, Grid,Bar


REMOTE_HOST = "https://pyecharts.github.io/assets/js"
def intelligence(request):
    def img1():
        gauge1 = Gauge("Yuanshui",width="100%")
        gauge1.add("", "m3/h", 15.3,angle_range=[180, 0],
            scale_range=[0, 30], is_legend_show=True)
        return gauge1.render_embed()
    def img2():
        gauge2 = Gauge("Zhoaye",width="100%")
        gauge2.add("zhaoye", "", 15.3,angle_range=[180, 0],
            scale_range=[0, 30], is_legend_show=False)
        return gauge2.render_embed()
    def img3():
        gauge3 = Gauge("jinshui",width="100%")
        gauge3.add("jinshui", "", 15.3,angle_range=[180, 0],
            scale_range=[0, 30], is_legend_show=False)
        return gauge3.render_embed()
    def img4():
        gauge4 = Gauge("Reflux1",width="100%")
        gauge4.add("wunihuiliu", "", 15.3,angle_range=[180, 0],
            scale_range=[0, 30], is_legend_show=False)
        return gauge4.render_embed()
    def img5():
        gauge5 = Gauge("Reflux2",width="100%")
        gauge5.add("hunheye", "", 15.3,angle_range=[180, 0],
            scale_range=[0, 30], is_legend_show=False)
        return gauge5.render_embed()
    def img6():
        from pyecharts import Bar
        bar = Bar("Level Height")
        attr = ["YUanshui", "Zhaoye", "Peishui", "Qingshui"]
        v1=[1.5,2,3,5.6]
        v2=[1.2,2.2,3.5,5.8]
        bar.add("Currently", attr, v1)
        bar.add("Yesterday", attr, v2, is_convert=True)
        return bar.render_embed()
    def img7():
        liquid2 = Liquid("height",width="100%")
        liquid2.add("Liquid", [0.6])
        return liquid2.render_embed()
    def img8():
        liquid3 = Liquid("height",width="100%")
        liquid3.add("Liquid", [0.6])
        return liquid3.render_embed()
    def img9():
        liquid4 = Liquid("height",width="100%")
        liquid4.add("Liquid", [0.6])
        return liquid4.render_embed()
    def img10():
        attr = ["A", "O1", "O2", "O3", "O4"]
        ph = [8.5, 8.3, 7.9, 7.8, 7.5]
        do = ['nan', 0.15, 0.65, 0.2, 0.35]
        line = Line("On-line Monitoring")
        line.add("pH", attr, ph, is_smooth=True,is_label_show=True)
        line.add("DO", attr, do, is_smooth=True,is_label_show=True)
        return line.render_embed()
      
    template = loader.get_template('intelligence.html')
    context = {
        "myechart1": img1(),
         "myechart2": img2(),
          "myechart3": img3(),
           "myechart4": img4(),
            "myechart5": img5(),
            "myechart6": img6(),
            "myechart7": img7(),
            "myechart8": img8(),
            "myechart9": img9(),
            "myechart10": img10()
    }
    return HttpResponse(template.render(context, request))

    

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
    try:
        contamination1=contamination.objects.get(date=today)
        a=''
        web_page=render(request,'diary.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    except:
        contamination2=contamination.objects.get(date=datetime.date(2018,1,1))
        a='NO Results!'
        web_page=render(request,'diary.html',{'contamination':contamination2,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    return web_page
def diary2(request):
    today=datetime.date.today()
    date1=today+datetime.timedelta(days=-1)
    date2=today+datetime.timedelta(days=-2)
    date3=today+datetime.timedelta(days=-3)
    date4=today+datetime.timedelta(days=-4)
    date5=today+datetime.timedelta(days=-5)
    date6=today+datetime.timedelta(days=-6)
    try:
        contamination1=contamination.objects.get(date=date1)
        a=''
        web_page=render(request,'diary2.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    except:
        contamination2=contamination.objects.get(date=datetime.date(2018,1,1))
        a='NO Results!'
        web_page=render(request,'diary2.html',{'contamination':contamination2,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    return web_page
def diary3(request):
    today=datetime.date.today()
    date1=today+datetime.timedelta(days=-1)
    date2=today+datetime.timedelta(days=-2)
    date3=today+datetime.timedelta(days=-3)
    date4=today+datetime.timedelta(days=-4)
    date5=today+datetime.timedelta(days=-5)
    date6=today+datetime.timedelta(days=-6)
    try:
        contamination1=contamination.objects.get(date=date2)
        a=''
        web_page=render(request,'diary3.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    except:
        contamination2=contamination.objects.get(date=datetime.date(2018,1,1))
        a='NO Results!'
        web_page=render(request,'diary3.html',{'contamination':contamination2,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    return web_page
def diary4(request):
    today=datetime.date.today()
    date1=today+datetime.timedelta(days=-1)
    date2=today+datetime.timedelta(days=-2)
    date3=today+datetime.timedelta(days=-3)
    date4=today+datetime.timedelta(days=-4)
    date5=today+datetime.timedelta(days=-5)
    date6=today+datetime.timedelta(days=-6)
    try:
        contamination1=contamination.objects.get(date=date3)
        a=''
        web_page=render(request,'diary4.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    except:
        contamination2=contamination.objects.get(date=datetime.date(2018,1,1))
        a='NO Results!'
        web_page=render(request,'diary4.html',{'contamination':contamination2,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    return web_page
def diary5(request):
    today=datetime.date.today()
    date1=today+datetime.timedelta(days=-1)
    date2=today+datetime.timedelta(days=-2)
    date3=today+datetime.timedelta(days=-3)
    date4=today+datetime.timedelta(days=-4)
    date5=today+datetime.timedelta(days=-5)
    date6=today+datetime.timedelta(days=-6)
    try:
        contamination1=contamination.objects.get(date=date4)
        a=''
        web_page=render(request,'diary5.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    except:
        contamination2=contamination.objects.get(date=datetime.date(2018,1,1))
        a='NO Results!'
        web_page=render(request,'diary5.html',{'contamination':contamination2,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    return web_page
def diary6(request):
    today=datetime.date.today()
    date1=today+datetime.timedelta(days=-1)
    date2=today+datetime.timedelta(days=-2)
    date3=today+datetime.timedelta(days=-3)
    date4=today+datetime.timedelta(days=-4)
    date5=today+datetime.timedelta(days=-5)
    date6=today+datetime.timedelta(days=-6)
    try:
        contamination1=contamination.objects.get(date=date5)
        a=''
        web_page=render(request,'diary6.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    except:
        contamination2=contamination.objects.get(date=datetime.date(2018,1,1))
        a='NO Results!'
        web_page=render(request,'diary6.html',{'contamination':contamination2,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    return web_page
def diary7(request):
    today=datetime.date.today()
    date1=today+datetime.timedelta(days=-1)
    date2=today+datetime.timedelta(days=-2)
    date3=today+datetime.timedelta(days=-3)
    date4=today+datetime.timedelta(days=-4)
    date5=today+datetime.timedelta(days=-5)
    date6=today+datetime.timedelta(days=-6)
    try:
        contamination1=contamination.objects.get(date=date6)
        a=''
        web_page=render(request,'diary7.html',{'contamination':contamination1,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    except:
        contamination2=contamination.objects.get(date=datetime.date(2018,1,1))
        a='NO Results!'
        web_page=render(request,'diary7.html',{'contamination':contamination2,'today':today,'date1':date1,'date2':date2,'date3':date3,'date4':date4,'date5':date5,'date6':date6,'a':a})
    return web_page

def data(request):
    
    session1=pull_session(url="http://139.196.84.157:8080/realtime1")
    script1=server_session(None,url="http://139.196.84.157:8080/realtime1",session_id=session1.id)
    session2=pull_session(url="http://139.196.84.157:8080/realtime2")
    script2=server_session(None,url="http://139.196.84.157:8080/realtime2",session_id=session2.id)
    session3=pull_session(url="http://139.196.84.157:8080/realtime3")
    script3=server_session(None,url="http://139.196.84.157:8080/realtime3",session_id=session3.id)
    return render(request, 'data.html', {'script1': script1,'script2': script2,'script3': script3})
def data_concentration(request):
    def datetime1(x):
        return np.array(x, dtype=np.datetime64)
    qs= contamination.objects.all().exclude(date=datetime.date(2018,1,1))
    df = read_frame(qs,fieldnames=['date','A_COD','O1_COD','O2_COD','O3_COD','O4_COD','Ef_COD'])
    TOOLS="hover"
    p1 = figure(x_axis_type="datetime", title="COD concentration @ Date (A)",width=800, height=150, tools=TOOLS)
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'COD concentration (mg/L)'
    p1.circle(datetime1(df['date']), df['A_COD'],fill_color='darkorange',line_color='darkorange')
    p1.line(datetime1(df['date']), df['A_COD'], color='darkorange')
    p2= figure(x_axis_type="datetime", title="COD concentration @ Date (O1)",width=800, height=150, tools=TOOLS)
    p2.grid.grid_line_alpha=0.3
    p2.xaxis.axis_label = 'Date'
    p2.yaxis.axis_label = 'COD concentration (mg/L)'  
    p2.line(datetime1(df['date']), df['O1_COD'], color='darkorange')
    p2.circle(datetime1(df['date']), df['O1_COD'],fill_color='darkorange',line_color='darkorange')
    p3= figure(x_axis_type="datetime", title="COD concentration @ Date (O2)",width=800, height=150, tools=TOOLS)
    p3.grid.grid_line_alpha=0.3
    p3.xaxis.axis_label = 'Date'
    p3.yaxis.axis_label = 'COD concentration (mg/L)'
    p3.circle(datetime1(df['date']), df['O2_COD'],fill_color='darkorange',line_color='darkorange')
    p3.line(datetime1(df['date']), df['O2_COD'], color='darkorange')
    p4= figure(x_axis_type="datetime", title="COD concentration @ Date (O3)",width=800, height=150, tools=TOOLS)
    p4.grid.grid_line_alpha=0.3
    p4.xaxis.axis_label = 'Date'
    p4.yaxis.axis_label = 'COD concentration (mg/L)'  
    p4.line(datetime1(df['date']), df['O3_COD'], color='darkorange')
    p4.circle(datetime1(df['date']), df['O3_COD'],fill_color='darkorange',line_color='darkorange')
    p5= figure(x_axis_type="datetime", title="COD concentration @ Date (O4)",width=800, height=150, tools=TOOLS)
    p5.grid.grid_line_alpha=0.3
    p5.xaxis.axis_label = 'Date'
    p5.yaxis.axis_label = 'COD concentration (mg/L)'  
    p5.line(datetime1(df['date']), df['O4_COD'], color='darkorange')
    p5.circle(datetime1(df['date']), df['O4_COD'],fill_color='darkorange',line_color='darkorange')
    p6= figure(x_axis_type="datetime", title="COD concentration @ Date (Ef)",width=800, height=150, tools=TOOLS)
    p6.grid.grid_line_alpha=0.3
    p6.xaxis.axis_label = 'Date'
    p6.yaxis.axis_label = 'COD concentration (mg/L)'  
    p6.line(datetime1(df['date']), df['Ef_COD'], color='darkorange')
    p6.circle(datetime1(df['date']), df['Ef_COD'],fill_color='darkorange',line_color='darkorange')

    p=gridplot([[p1],[p2],[p3],[p4],[p5],[p6]])

    script1, div1 = components(p, CDN)
    return render(request, 'data_concentration.html', {'script1': script1, 'div1': div1})
def data_concentration2(request):
    def datetime1(x):
        return np.array(x, dtype=np.datetime64)
    qs= contamination.objects.all().exclude(date=datetime.date(2018,1,1))
    df = read_frame(qs,fieldnames=['date','A_NH4','O1_NH4','O2_NH4','O3_NH4','O4_NH4','Ef_NH4'])
    TOOLS="hover"
    p1 = figure(x_axis_type="datetime", title="Ammonia @ Date (A)",width=800, height=150, tools=TOOLS)
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Ammonia(mg/L)'
    p1.circle(datetime1(df['date']), df['A_NH4'],fill_color='orangered',line_color='orangered')
    p1.line(datetime1(df['date']), df['A_NH4'], color='orangered')
    p2= figure(x_axis_type="datetime", title="Ammonia @ Date (O1)",width=800, height=150, tools=TOOLS)
    p2.grid.grid_line_alpha=0.3
    p2.xaxis.axis_label = 'Date'
    p2.yaxis.axis_label = 'Ammonia (mg/L)'  
    p2.line(datetime1(df['date']), df['O1_NH4'], color='orangered')
    p2.circle(datetime1(df['date']), df['O1_NH4'],fill_color='orangered',line_color='orangered')
    p3= figure(x_axis_type="datetime", title="Ammonia @ Date (O2)",width=800, height=150, tools=TOOLS)
    p3.grid.grid_line_alpha=0.3
    p3.xaxis.axis_label = 'Date'
    p3.yaxis.axis_label = 'Ammonia (mg/L)'
    p3.circle(datetime1(df['date']), df['O2_NH4'],fill_color='orangered',line_color='orangered')
    p3.line(datetime1(df['date']), df['O2_NH4'], color='orangered')
    p4= figure(x_axis_type="datetime", title="Ammonia @ Date (O3)",width=800, height=150, tools=TOOLS)
    p4.grid.grid_line_alpha=0.3
    p4.xaxis.axis_label = 'Date'
    p4.yaxis.axis_label = 'Ammonia (mg/L)'  
    p4.line(datetime1(df['date']), df['O3_NH4'], color='orangered')
    p4.circle(datetime1(df['date']), df['O3_NH4'],fill_color='orangered',line_color='orangered')
    p5= figure(x_axis_type="datetime", title="Ammonia @ Date (O4)",width=800, height=150, tools=TOOLS)
    p5.grid.grid_line_alpha=0.3
    p5.xaxis.axis_label = 'Date'
    p5.yaxis.axis_label = 'Ammonia (mg/L)'  
    p5.line(datetime1(df['date']), df['O4_NH4'], color='orangered')
    p5.circle(datetime1(df['date']), df['O4_NH4'],fill_color='orangered',line_color='orangered')
    p6= figure(x_axis_type="datetime", title="Ammonia @ Date (Ef)",width=800, height=150, tools=TOOLS)
    p6.grid.grid_line_alpha=0.3
    p6.xaxis.axis_label = 'Date'
    p6.yaxis.axis_label = 'Ammonia (mg/L)'  
    p6.line(datetime1(df['date']), df['Ef_NH4'], color='orangered')
    p6.circle(datetime1(df['date']), df['Ef_NH4'],fill_color='orangered',line_color='orangered')

    p=gridplot([[p1],[p2],[p3],[p4],[p5],[p6]])

    script1, div1 = components(p, CDN)
    return render(request, 'data_concentration2.html', {'script1': script1, 'div1': div1})
def data_concentration3(request):
    def datetime1(x):
        return np.array(x, dtype=np.datetime64)
    qs= contamination.objects.all().exclude(date=datetime.date(2018,1,1))
    df = read_frame(qs,fieldnames=['date','A_NO2','O1_NO2','O2_NO2','O3_NO2','O4_NO2','Ef_NO2'])
    TOOLS="hover"
    p1 = figure(x_axis_type="datetime", title="Nitrite @ Date (A)",width=800, height=150, tools=TOOLS)
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Nitrite(mg/L)'
    p1.circle(datetime1(df['date']), df['A_NO2'],fill_color='hotpink',line_color='hotpink')
    p1.line(datetime1(df['date']), df['A_NO2'], color='hotpink')
    p2= figure(x_axis_type="datetime", title="Nitrite @ Date (O1)",width=800, height=150, tools=TOOLS)
    p2.grid.grid_line_alpha=0.3
    p2.xaxis.axis_label = 'Date'
    p2.yaxis.axis_label = 'Nitrite (mg/L)'  
    p2.line(datetime1(df['date']), df['O1_NO2'], color='hotpink')
    p2.circle(datetime1(df['date']), df['O1_NO2'],fill_color='hotpink',line_color='hotpink')
    p3= figure(x_axis_type="datetime", title="Nitrite @ Date (O2)",width=800, height=150, tools=TOOLS)
    p3.grid.grid_line_alpha=0.3
    p3.xaxis.axis_label = 'Date'
    p3.yaxis.axis_label = 'Nitrite (mg/L)'
    p3.circle(datetime1(df['date']), df['O2_NO2'],fill_color='hotpink',line_color='hotpink')
    p3.line(datetime1(df['date']), df['O2_NO2'], color='hotpink')
    p4= figure(x_axis_type="datetime", title="Nitrite @ Date (O3)",width=800, height=150, tools=TOOLS)
    p4.grid.grid_line_alpha=0.3
    p4.xaxis.axis_label = 'Date'
    p4.yaxis.axis_label = 'Nitrite (mg/L)'  
    p4.line(datetime1(df['date']), df['O3_NO2'], color='hotpink')
    p4.circle(datetime1(df['date']), df['O3_NO2'],fill_color='hotpink',line_color='hotpink')
    p5= figure(x_axis_type="datetime", title="Nitrite @ Date (O4)",width=800, height=150, tools=TOOLS)
    p5.grid.grid_line_alpha=0.3
    p5.xaxis.axis_label = 'Date'
    p5.yaxis.axis_label = 'Nitrite (mg/L)'  
    p5.line(datetime1(df['date']), df['O4_NO2'], color='hotpink')
    p5.circle(datetime1(df['date']), df['O4_NO2'],fill_color='hotpink',line_color='hotpink')
    p6= figure(x_axis_type="datetime", title="Nitrite @ Date (Ef)",width=800, height=150, tools=TOOLS)
    p6.grid.grid_line_alpha=0.3
    p6.xaxis.axis_label = 'Date'
    p6.yaxis.axis_label = 'Nitrite (mg/L)'  
    p6.line(datetime1(df['date']), df['Ef_NO2'], color='hotpink')
    p6.circle(datetime1(df['date']), df['Ef_NO2'],fill_color='hotpink',line_color='hotpink')

    p=gridplot([[p1],[p2],[p3],[p4],[p5],[p6]])

    script1, div1 = components(p, CDN)
    return render(request, 'data_concentration3.html', {'script1': script1, 'div1': div1})
def data_advance(request):
    
    session=pull_session(url="http://139.196.84.157:8080/offline1")
    script=server_session(None,url="http://139.196.84.157:8080/offline1",session_id=session.id)
    return render(request, 'data_advance.html', {'script': script})

def intelligence2(request):


    gram_color = {
        "positive" : "#aeaeb8",
        "negative" : "#e69584",
    }


    width = 400
    height = 400
    inner_radius = 160
    outer_radius = 360


    big_angle = 2.0 * np.pi / 5
    small_angle = big_angle/3 

    p = figure(plot_width=width, plot_height=height, title="",
        x_axis_type=None, y_axis_type=None,
        x_range=(-420, 420), y_range=(-420, 420),
        min_border=0, outline_line_color="black",
        background_fill_color="#f0e1d2",tools="")


    # annular wedges
    angles = np.array([np.pi*1/10,np.pi*1/2,np.pi*9/10,np.pi*13/10,np.pi*17/10])
    colors=[ 'firebrick','lightcoral','lightsalmon']
    p.annular_wedge(0, 0, inner_radius, 200,np.pi/10000,-np.pi/10000,color=colors[0])
    p.annular_wedge(0, 0, 200, 280,np.pi/10000,-np.pi/10000,color=colors[1])
    p.annular_wedge(0, 0, 280, outer_radius,np.pi/10000,-np.pi/10000,color=colors[2])
    p.annular_wedge(0, 0, outer_radius, outer_radius+20,np.pi/10000,-np.pi/10000,color="#f0e1d2")
    # radial axes
    p.annular_wedge(0, 0, inner_radius, outer_radius, big_angle+angles, big_angle+angles, color="black")
    
    p.annular_wedge(0, 0, inner_radius, 250,-54/180*np.pi+small_angle, -54/180*np.pi+2*small_angle,color='lightsteelblue',legend='Nitrification')
    p.annular_wedge(0, 0, inner_radius, 220,-126/180*np.pi+small_angle, -126/180*np.pi+2*small_angle,color='skyblue',legend='Denitrification')
    p.annular_wedge(0, 0, inner_radius, 200,-198/180*np.pi+small_angle, -198/180*np.pi+2*small_angle,color='deepskyblue',legend='Alkalinity Balance')
    p.annular_wedge(0, 0, inner_radius, 310,-270/180*np.pi+small_angle, -270/180*np.pi+2*small_angle,color='dodgerblue',legend='Carbon Removal')
    p.annular_wedge(0, 0, inner_radius, 260,-342/180*np.pi+small_angle, -342/180*np.pi+2*small_angle,color='mediumblue',legend='Influent Stabilization')

    p.legend.location = "bottom_left"
    p.text(-110, 0, text=["78"],text_font_size="65pt", text_align="left", text_baseline="middle")
    p.text(-62, -95, text=["Overoll"],text_font_size="13pt", text_align="left", text_baseline="middle")

    radii = np.array([160,200,280,360])
    p.circle(0, 0, radius=radii, fill_color=None, line_color="white")
    

    script, div = components(p, CDN)
    return render(request, 'intelligence2.html',{'script': script, 'div': div})
def contact(request):
    return render(request, 'contact.html')
# Create your views here.
