import pandas as pd
import plotly.express as ps
import plotly.figure_factory as ff

df = pd.read_csv("Students.csv")
WeightData = df["Weight(Pounds)"].tolist()

fig = ff.create_distplot([WeightData], ["Weight Data"], show_hist = False)
fig.show()