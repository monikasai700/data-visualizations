import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
df = pd.read_csv('Book1.csv')
df.head()
trace1 = go.Scatter(
                    x=df['Engine Size'], y=df['logx'], # Data
                    mode='lines', name='logx' # Additional options
                   )
trace2 = go.Scatter(x=df['Cyl'], y=df['HP'], mode='lines', name='sinx' )
trace3 = go.Scatter(x=df['HP'], y=df['AverageMPG'], mode='lines', name='cosx')
trace4 = go.Scatter(x=df['AverageMPG'], y=df['Cyl'], mode='lines', name='cosx')
layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3,trace4], layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='simple-plot-from-csv')