import pandas as p
import plotly_express as pe

df = p.read_csv('data.csv')
graph = pe.scatter(df, x='date', y='cases', color='country',)
graph.show()
