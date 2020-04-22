import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


path = 'data/'
file_name = 'datalog'
file = path+file_name + '.csv'

df = pd.read_csv(file)

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
file_tem = 'data_plot/'+file_name + '_tem.jpeg'
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
file_hum = 'data_plot/'+ file_name + '_hum.jpeg'
fig.write_image(file_hum)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['PhotoRes'], name="Luz solar",
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
file_luz = 'data_plot/' + file_name + '_luz.jpeg'
fig.write_image(file_luz)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['MQ2'], name="Metano",
                         line_color='red'))
fig.update_layout(
    title="Methane analysis",
    yaxis_title="Concentration (u.a.)",
    font=dict(
        size=20,
    )
)
fig.update_layout(width = 1600, height = 900)
fig.show()
file_mq2 = 'data_plot/' + file_name + '_mq2.jpeg'
fig.write_image(file_mq2)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['MQ7'], name="CO2",
                         line_color='red'))
fig.update_layout(
    title="CO2 analysis",
    yaxis_title="Concentration (u.a.)",
    font=dict(
        size=20,
    )
)
fig.update_layout(width = 1600, height = 900)
fig.show()
file_mq7 = 'data_plot/' + file_name + '_mq2.jpeg'
fig.write_image(file_mq7)

#%% Unified subplots
fig = make_subplots(rows=3, cols=1)

fig.append_trace(go.Scatter(x=df.index, y=df['T'], name ="Temperatura"
), row=1, col=1)
fig.update_layout(title="Stacked plot", yaxis_title="Temperatura (°C)",
    font=dict(size=20,))

fig.append_trace(go.Scatter(x=df.index, y=df['H'], name = "Humedad"),
row=2, col=1)
fig.update_yaxes(title_text="Humedad (%)", row=2, col=1)

fig.append_trace(go.Scatter(x=df.index, y=df['PhotoRes'], name = "Luz"
), row=3, col=1)
fig.update_yaxes(title_text="Penumbra (u.a.)", row=3, col=1)

fig.update_layout(height=900, width=1600, title_text="Stacked subplots")
fig.show()
file_stack = 'data_plot/' + file_name + '_stack.jpeg'
fig.write_image(file_stack)

fig = make_subplots(rows=2, cols=1)

fig.append_trace(go.Scatter(x=df.index, y=df['MQ2'], name ="Methane"
), row=1, col=1)
fig.update_layout(
    title="Methane Analysis",
    yaxis_title="Concentration (u.a.)",
    font=dict(
        size=20,
    )
)
fig.append_trace(go.Scatter(x=df.index, y=df['MQ7'], name = "CO2"
), row=2, col=1)
fig.update_yaxes(title_text="Concentration (u.a.)", row=2, col=1)

fig.update_layout(height=900, width=1600, title_text="Stacked subplots")
fig.show()
file_stack = 'data_plot/' + file_name + '_stack_2.jpeg'
fig.write_image(file_stack)
