from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np
import pandas as pd
import plotly.graph_objects as go

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
df = pd.read_csv('./Top3QBelgiumGP2021.csv')
df.head()


driver = st.selectbox('Pick driver', ['VER', 'PER', 'HAM', 'NOR', 'OCO', 'STR', 'GAS', 'VET', 'RUS', 'ALO', 'BOT', 'LAT', 'RIC', 'SAI', 'MSC', 'LEC', 'TSU', 'GIO', 'MAZ', 'RAI'])
dataDriver = df.loc[df['Driver'] == driver]

lap = st.slider("Choose lap", 1, 30)
dataLap = dataDriver.loc[dataDriver['Lap'] == lap]

color_chan = "Speed"

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
