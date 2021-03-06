# -*- coding: utf-8 -*-
"""Final Project_Visdat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14phwMiog8rLoQ-Rf5ltj_ThygVwlq7w5

```
**Final Project Visualisasi Data**
Rizky Haffiyan Roseno (1301194042)
Fadhilah Nadia Puteri (1301194200)
```
"""

# Import Library and Data
from bokeh.io import output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import ColumnDataSource, GroupFilter, CDSView, HoverTool, Div
from bokeh.layouts import column, widgetbox
import pandas as pd
import numpy as np

#import data
df = pd.read_csv('/content/bursa_saham2.csv', parse_dates=['date'])
#df = df.rename(columns = {'Adj Close': 'Adj_Close'}, inplace = False)
df.head()

"""# **Sort Data**"""

#sort data
source = ColumnDataSource(df)

filter_ai = [GroupFilter(column_name='name', group='AALI')]
source_ai = CDSView(source=source,filters=filter_ai)

filter_am = [GroupFilter(column_name='name', group='ANTM')]
source_am = CDSView(source=source,filters=filter_am)

filter_bp = [GroupFilter(column_name='name', group='BAPI')]
source_bp = CDSView(source=source,filters=filter_bp)

#set circle info
circle_data = {'source': source, 'size': 3, 'alpha': 0.7, 'selection_color':'black'}

circle_ai = {'view': source_ai, 'color': 'red', 'legend_label': 'AALI'}

circle_am = {'view': source_am, 'color': 'green', 'legend_label': 'ANTM'}

circle_bp = {'view': source_bp, 'color': 'blue', 'legend_label': 'BAPI'}

"""**Adj Close (lvl 1)**"""

#create figure
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
figure1 = figure(title= 'Adjusted Close Data',x_axis_type='datetime',x_axis_label='date', y_axis_label= 'Close Data',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
figure1.circle(x='date', y='close', **circle_data, **circle_ai)
figure1.circle(x='date', y='close', **circle_data, **circle_am)
figure1.circle(x='date', y='close', **circle_data, **circle_bp)

#add hover
tooltips= [ ('Name','@name'),('Adj_Close', '@close') ]
hover_glyph = figure1.circle(x='date', y= 'close' , source=source,size=3, alpha=0, hover_fill_color='black', hover_alpha=0.5)
figure1.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

"""# Volume (lvl 2)"""

#create figure
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
figure2 = figure(title= 'Volume Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Volume',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
figure2.circle(x='date', y='volume', **circle_data, **circle_ai)
figure2.circle(x='date', y='volume', **circle_data, **circle_am)
figure2.circle(x='date', y='volume', **circle_data, **circle_bp)

#add hover
tooltips= [ ('Name','@name'),('Volume', '@volume') ]
hover_glyph = figure2.circle(x='date', y= 'volume' , source=source,size=3, alpha=0,hover_fill_color='black', hover_alpha=0.5)
figure2.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

"""# Day Perc Change (lvl 2)"""

#create figure
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
figure3 = figure(title= 'Change Data Per DAY',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Change per DAY',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
figure3.circle(x='date', y='change', **circle_data, **circle_ai)
figure3.circle(x='date', y='change', **circle_data, **circle_am)
figure3.circle(x='date', y='change', **circle_data, **circle_bp)

#add hover
tooltips= [ ('Name','@name'),('Day_Perc_Change', '@change') ]
hover_glyph = figure3.circle(x='date', y= 'change' , source=source,size=3, alpha=0,hover_fill_color='black', hover_alpha=0.5)
figure3.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

#create figure
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
figure4 = figure(title= 'Value DATA',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'VALUE DATA',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
figure4.circle(x='date', y='value', **circle_data, **circle_ai)
figure4.circle(x='date', y='value', **circle_data, **circle_am)
figure4.circle(x='date', y='value', **circle_data, **circle_bp)

#add hover
tooltips= [ ('Name','@name'),('Value', '@value') ]
hover_glyph = figure4.circle(x='date', y= 'value' , source=source,size=3, alpha=0,hover_fill_color='black', hover_alpha=0.5)
figure3.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

"""# Hide Index (lvl 3)"""

#hide data via legend
figure1.legend.click_policy = 'hide'
figure1.legend.location= 'top_right'

figure2.legend.click_policy = 'hide'
figure2.legend.location= 'top_right'

figure3.legend.click_policy = 'hide'
figure2.legend.location= 'top_right'

figure4.legend.click_policy = 'hide'
figure2.legend.location= 'top_right'

"""# Configure Panel"""

#add title
isi = """<h1>Visualisasi Data Interaktif Bursa Saham</h1>
<h3><i>Click Legend to HIDE Data</i><h3>"""
title = Div(text=isi)
#add widget panel and tab
figure1_panel = Panel(child=figure1, title='Adjusted Close Data')
figure2_panel = Panel(child=figure2, title='Volume Data')
figure3_panel = Panel(child=figure3, title='Day_Perc_Change Data')
figure4_panel = Panel(child=figure4, title='Value DATA')
tab = Tabs(tabs=[figure1_panel, figure2_panel, figure3_panel, figure4_panel])
#add layout
show(column(title,tab))