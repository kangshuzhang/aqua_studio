#import libraries
from bokeh.io import curdoc
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import random
 
#create figure
f=figure(plot_width=900,plot_height=300,title='Realtime Monitoring_pH')

#create columndatasource
source=ColumnDataSource(data=dict(x=[0],y1=[8.5],y2=[8.1],y3=[7.9],y4=[7.4]))
 
#create glyphs
f.circle(x='x',y='y1',size=5,fill_color='lightsteelblue',source=source)
f.circle(x='x',y='y2',size=5,fill_color='skyblue',source=source)
f.circle(x='x',y='y3',size=5,fill_color='dodgerblue',source=source)
f.circle(x='x',y='y4',size=5,fill_color='mediumblue',source=source)
f.line(x='x',y='y1',line_width=2,line_color='lightsteelblue',source=source,legend='O1')
f.line(x='x',y='y2',line_width=2,line_color='skyblue',source=source,legend='O2')
f.line(x='x',y='y3',line_width=2,line_color='dodgerblue',source=source,legend='O3')
f.line(x='x',y='y4',line_width=2,line_color='mediumblue',source=source,legend='O4')
f.xaxis.axis_label = 'Datetime'
f.yaxis.axis_label = 'pH'
f.title.text_font_size = "20px"
f.legend.location = "top_left"

#create periodic function


def update():
    new_data=dict(x=[source.data['x'][-1]+1],y1=[source.data['y1'][-1]+(random()-0.5)*0.2],y2=[source.data['y2'][-1]+(random()-0.5)*0.2]
    ,y3=[source.data['y3'][-1]+(random()-0.5)*0.2],y4=[source.data['y4'][-1]+(random()-0.5)*0.2])
    source.stream(new_data,rollover=20)


 
#add figure to curdoc and configure callback

curdoc().add_root(f)
curdoc().add_periodic_callback(update,1000)