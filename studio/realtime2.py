#import libraries
from bokeh.io import curdoc
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import random
 
#create figure
f=figure(plot_width=900,plot_height=300,title='Realtime Monitoring_Dissolve Oxygen')

#create columndatasource
source=ColumnDataSource(data=dict(x=[0],y1=[0.15],y2=[0.5],y3=[0.15],y4=[0.3]))
 
#create glyphs
f.circle(x='x',y='y1',size=5,fill_color='salmon',source=source)
f.circle(x='x',y='y2',size=5,fill_color='darkred',source=source)
f.circle(x='x',y='y3',size=5,fill_color='pink',source=source)
f.circle(x='x',y='y4',size=5,fill_color='crimson',source=source)
f.line(x='x',y='y1',line_width=2,line_color='salmon',source=source,legend='O1')
f.line(x='x',y='y2',line_width=2,line_color='darkred',source=source,legend='O2')
f.line(x='x',y='y3',line_width=2,line_color='pink',source=source,legend='O3')
f.line(x='x',y='y4',line_width=2,line_color='crimson',source=source,legend='O4')
f.xaxis.axis_label = 'Datetime'
f.yaxis.axis_label = 'Dissolve Oxygen (mg/L)'
f.title.text_font_size = "20px"
f.legend.location = "top_left"

#create periodic function


def update():
    new_data=dict(x=[source.data['x'][-1]+1],y1=[source.data['y1'][-1]+(random()-0.5)*0.05],y2=[source.data['y2'][-1]+(random()-0.5)*0.05]
    ,y3=[source.data['y3'][-1]+(random()-0.5)*0.05],y4=[source.data['y4'][-1]+(random()-0.5)*0.05])
    source.stream(new_data,rollover=20)


 
#add figure to curdoc and configure callback

curdoc().add_root(f)
curdoc().add_periodic_callback(update,1000)