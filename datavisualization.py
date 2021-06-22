import pandas as pd
import plotly.express as px


df=pd.read_csv("Covid Data.csv")
print(df)

fig = px.scatter(df,x="date",y="cases",color="country", title="Covid cases of countries")

fig.show()
