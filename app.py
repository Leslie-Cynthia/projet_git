import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# loading of data
df=pd.read_csv("data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["price"] = pd.to_numeric(df["price"],errors='coerce')

#last value
latest = df.iloc[-1]
latest_price = latest["price"]
latest_time=latest["timestamp"]

#daily data
today = pd.Timestamp.today().date()
df_today = df[df["timestamp"].dt.date == today]


daily_avg = df_today["price"].mean()
daily_min = df_today["price"].min()
daily_max = df_today["price"].max()


#graph creation
fig = px.line(df, x="timestamp", y="price", title="Evolution of bitcoin price (EUR)")

# app dash creation
app= Dash(__name__)

app.layout=html.Div([
	html.H1("Dashboard Bitcoin - Projet Git"),
	html.H2(f"Dernier prix: {latest_price} EUR (à {latest_time.strftime('%H:%M:%S')})"),
	dcc.Graph(figure=fig),
	html.Div([
		html.H3(" Daily report"),
		html.P(f"Average : {daily_avg:.2f} EUR"),
		html.P(f"Min : {daily_min:.2f} EUR"),
		html.P(f"Max : {daily_max:.2f} EUR"),
	])
])


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8050)













