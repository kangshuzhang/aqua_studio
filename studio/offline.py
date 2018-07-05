from django.shortcuts import render
import studio
from models import contamination 
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
import datetime
import pandas as pd
from django_pandas.io import read_frame

def datetime1(x):
        return np.array(x, dtype=np.datetime64)
qs= contamination.objects.all().exclude(date=datetime.date(2018,1,1))
df = read_frame(qs,fieldnames=['date','A_Tem','O1_Tem','O2_Tem','O3_Tem','O4_Tem','A_pH','O1_pH','O2_pH','O3_pH','O4_pH','A_Do','O1_Do','O2_Do','O3_Do','O4_Do',
'A_COD','O1_COD','O2_COD','O3_COD','O4_COD','Cf_COD','Ef_COD','A_NH4','O1_NH4','O2_NH4','O3_NH4','O4_NH4','Cf_NH4','Ef_NH4','A_NO2','O1_NO2','O2_NO2','O3_NO2','O4_NO2','Cf_NO2','Ef_NO2','A_NO3','O1_NO3','O2_NO3','O3_NO3','O4_NO3','Cf_NO3','Ef_NO3',
'A_MLSS','O1_MLSS','O2_MLSS','O3_MLSS','O4_MLSS'])

    


DEFAULT = ['date','A_Tem','O1_Tem','O2_Tem','O3_Tem','O4_Tem','A_pH','O1_pH','O2_pH','O3_pH','O4_pH','A_Do','O1_Do','O2_Do','O3_Do','O4_Do',
'A_COD','O1_COD','O2_COD','O3_COD','O4_COD','Cf_COD','Ef_COD','A_NH4','O1_NH4','O2_NH4','O3_NH4','O4_NH4','Cf_NH4','Ef_NH4','A_NO2','O1_NO2','O2_NO2','O3_NO2','O4_NO2','Cf_NO2','Ef_NO2','A_NO3','O1_NO3','O2_NO3','O3_NO3','O4_NO3','Cf_NO3','Ef_NO3',
'A_MLSS','O1_MLSS','O2_MLSS','O3_MLSS','O4_MLSS']

def nix(val, lst):
        return [x for x in lst if x != val]


def load_ticker(ticker):
        data = df.set_index('date')
        return pd.DataFrame({ticker: data[ticker], ticker+'_returns': data[ticker].diff()})


def get_data(t1, t2):
        df1 = load_ticker(t1)
        df2 = load_ticker(t2)
        data = pd.concat([df1, df2], axis=1)
        data = data.dropna()
        data['t1'] = data[t1]
        data['t2'] = data[t2]
        data['t1_returns'] = data[t1+'_returns']
        data['t2_returns'] = data[t2+'_returns']
        return data

    # set up widgets

stats = PreText(text='', width=500)
ticker1 = Select(value='O1_COD', options=nix('O1_COD', DEFAULT))
ticker2 = Select(value='O2_COD', options=nix('O2_COD', DEFAULT))

    # set up plots

source = ColumnDataSource(data=dict(date=[], t1=[], t2=[], t1_returns=[], t2_returns=[]))
source_static = ColumnDataSource(data=dict(date=[], t1=[], t2=[], t1_returns=[], t2_returns=[]))
tools = 'pan,wheel_zoom,xbox_select,reset'

corr = figure(plot_width=350, plot_height=350,tools='pan,wheel_zoom,box_select,reset')
corr.circle('t1_returns', 't2_returns', size=2, source=source,selection_color="orange", alpha=0.6, nonselection_alpha=0.1, selection_alpha=0.4)

ts1 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ts1.line('date', 't1', source=source_static)
ts1.circle('date', 't1', size=1, source=source, color=None, selection_color="orange")

ts2 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ts2.x_range = ts1.x_range
ts2.line('date', 't2', source=source_static)
ts2.circle('date', 't2', size=1, source=source, color=None, selection_color="orange")

    # set up callbacks

def ticker1_change(attrname, old, new):
        ticker2.options = nix(new, DEFAULT)
        update()

def ticker2_change(attrname, old, new):
        ticker1.options = nix(new, DEFAULT)
        update()

def update(selected=None):
        t1, t2 = ticker1.value, ticker2.value

        data = get_data(t1, t2)
        source.data = source.from_df(data[['t1', 't2', 't1_returns', 't2_returns']])
        source_static.data = source.data

        update_stats(data, t1, t2)

        corr.title.text = '%s returns vs. %s returns' % (t1, t2)
        ts1.title.text, ts2.title.text = t1, t2

def update_stats(data, t1, t2):
        stats.text = str(data[[t1, t2, t1+'_returns', t2+'_returns']].describe())

ticker1.on_change('value', ticker1_change)
ticker2.on_change('value', ticker2_change)

def selection_change(attrname, old, new):
        t1, t2 = ticker1.value, ticker2.value
        data = get_data(t1, t2)
        selected = source.selected.indices
        if selected:
            data = data.iloc[selected, :]
        update_stats(data, t1, t2)

source.on_change('selected', selection_change)

    # set up layout
widgets = column(ticker1, ticker2, stats)
main_row = row(corr, widgets)
series = column(ts1, ts2)
layout = column(main_row, series)

    # initialize
update()

curdoc().add_root(layout)