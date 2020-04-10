import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#file = 'data_THL.csv'
file_name = 'data_THL_abr-06-2020'
file = file_name + '.csv'

df = pd.read_csv(file)

df.index = df['time']
df.index = pd.to_datetime(df.index).strftime('%Y-%m-%d %H:%M:%S')

#%% Separated plots
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['T'], name="Temperatura",
                         line_color='red'))
fig.update_layout(
    title="Temperatura Dormitorio",
    yaxis_title="Temperatura (C)",
    font=dict(
        size=20,
    )
)
fig.update_layout(width = 1600, height = 900)
fig.show()
file_tem = file_name + '_tem.jpeg'
fig.write_image(file_tem)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['H'], name="Humedad",
                         line_color='red'))
fig.update_layout(
    title="Humedad Dormitorio",
    yaxis_title="Humedad (%)",
    font=dict(
        size=20,
    )
)
fig.update_layout(width = 1600, height = 900)
fig.show()
file_hum = file_name + '_hum.jpeg'
fig.write_image(file_hum)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['L'], name="Luz solar",
                         line_color='red'))
fig.update_layout(
    title="Luz Dormitorio",
    yaxis_title="Oscuridad (u.a.)",
    font=dict(
        size=20,
    )
)
fig.update_layout(width = 1600, height = 900)
fig.show()
file_luz = file_name + '_luz.jpeg'
fig.write_image(file_luz)

# Whole subplots
fig = make_subplots(rows=3, cols=1)

fig.append_trace(go.Scatter(x=df.index, y=df['T'], name ="Temperatura"
), row=1, col=1)
fig.update_layout(
    title="Temperatura",
    yaxis_title="Temperatura (°C)",
    font=dict(
        size=20,
    )
)
fig.append_trace(go.Scatter(x=df.index, y=df['H'], name = "Humedad"
), row=2, col=1)

fig.append_trace(go.Scatter(x=df.index, y=df['L'], name = "Luz"
), row=3, col=1)

fig.update_layout(height=900, width=1600, title_text="Stacked subplots")
fig.show()
file_stack = file_name + '_stack.jpeg'
fig.write_image(file_stack)
