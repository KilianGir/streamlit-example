from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

"""
# First motorsport data app

All qualifications laps for top3 drivers in Formula 1 2021 Belgian GP:
"""
df = pd.read_csv('./Top3QBelgiumGP2021.csv')
df.head()


driver = st.selectbox('Pick driver', ['VER','HAM','RUS'])
dataDriver = df.loc[df['Driver'] == driver]

maxLap = int(dataDriver['Lap'].max())
lap = st.slider("Choose lap", 1, maxLap)
dataLap = dataDriver.loc[dataDriver['Lap'] == lap]

color_chan = st.selectbox('Select color channel', ['RPM','Speed','nGear','Throttle','Brake','DRS'])

plotX = dataLap['X']
plotY = dataLap['Y']
plotColor = dataLap[color_chan] 


fig = go.Figure(data=go.Scatter(
    x = plotX,
    y = plotY,
    hovertext = plotColor,
    mode='markers',
    marker=dict(
        size=4,
        color = plotColor, #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
))

fig.update_layout(
    width = 800,
    height = 800
)
fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1,
  )

st.plotly_chart(fig, use_container_width=True)
