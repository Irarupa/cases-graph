import pandas as pd
import plotly.express as px 

df_graph = pd.read_csv('data.csv')
fig  = px.line(df_graph, x= 'date', y = 'cases',color = 'country',title = 'Number of everyday cases in different countries')
fig.show()