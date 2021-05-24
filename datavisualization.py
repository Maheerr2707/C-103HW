import pandas as pd
import plotly.express as px


df=pd.read_csv("Covid data.csv")
print(df)

fig = px.line(df,x="date",y="cases",color="country",title="Covid cases of countries")
fig.show()
