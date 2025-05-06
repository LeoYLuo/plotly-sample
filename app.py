#!/usr/bin/env python
# coding: utf-8

# In[6]:


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Example data → you can replace with your real data
df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [10, 20, 30, 40]})
fig = px.line(df, x='x', y='y')

app.layout = html.Div([
    html.H1("CTR Dashboard Example"),
    dcc.Graph(figure=fig)
])

server = app.server  # required for deployment

if __name__ == '__main__':
    app.run(debug=True)


# In[2]:


app.run(jupyter_mode="external")


# In[4]:


pip freeze > requirements.txt

