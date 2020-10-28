import pandas as pd
import plotly.express as ps
import plotly.figure_factory as ff

df = pd.read_csv("Students.csv")
HeightData = df["Height(Inches)"].tolist()

fig = ff.create_distplot([HeightData], ["Height Data"], show_hist = False)
fig.show()