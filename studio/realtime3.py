#import libraries
from bokeh.io import curdoc
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import random
 
#create figure
f=figure(plot_width=900,plot_height=300,title='Realtime Monitoring_Flow')

#create columndatasource
source=ColumnDataSource(data=dict(x=[0],y1=[160],y2=[800]))
 
#create glyphs
f.circle(x='x',y='y1',size=5,fill_color='yellowgreen',source=source)
f.circle(x='x',y='y2',size=5,fill_color='mediumseagreen',source=source)
f.line(x='x',y='y1',line_width=2,line_color='yellowgreen',source=source,legend='Influent')
f.line(x='x',y='y2',line_width=2,line_color='mediumseagreen',source=source,legend='Reflux')
f.xaxis.axis_label = 'Datetime'
f.yaxis.axis_label = 'Flow (L/min)'
f.title.text_font_size = "20px"
f.legend.location = "top_left"

#create periodic function


def update():
    new_data=dict(x=[source.data['x'][-1]+1],y1=[source.data['y1'][-1]+(random()-0.5)*10],y2=[source.data['y2'][-1]+(random()-0.5)*40])
    source.stream(new_data,rollover=20)


 
#add figure to curdoc and configure callback

curdoc().add_root(f)
curdoc().add_periodic_callback(update,1000)