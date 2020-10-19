# -*- coding: utf-8 -*-

"""
Created on 10/17/2020

@author: mlr7

Run this app with `python app.py` and

visit http://127.0.0.1:8050/ in your web browser.
Close app with 'ctrl + c'
"""
## Imports ##

import pandas as pd

import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

## Configure Viz ##

app = dash.Dash(__name__)

## Data Ingest ##

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df_wide = pd.DataFrame({'Year': [1988, 2020],
                  'BA': [0.248, 0.256],
                  'SLG': [0.354, 0.483],
                  'ERA': [2.96, 3.02]})

# Convert dataframe to long format

df_long = pd.melt(df_wide, id_vars=['Year'], var_name='Stat',  value_name='Value')
df_long['Year'] = df_long['Year'].astype(str)

## Create Visualization

fig = px.bar(df_long, x="Stat", y="Value", color="Year", barmode="group")

## Create the Data App ##

app.layout = html.Div(children=[
    html.H1(children='Dodgers: 1988 vs 2020'),

    html.Div(children='''
        Comparing key stats of the 1988 World Series Champion Dodgers to the 2020 Dodgers
    '''),

    dcc.Graph(
        id='dodger1-graph',
        figure=fig
    )
])

## Create main ## 

if __name__ == '__main__':
    app.run_server(debug=True)
    



