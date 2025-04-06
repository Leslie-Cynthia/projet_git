import pandas as pd
from dash import Dash, dcc, html, dcc, Output, Input
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

app.layout = html.Div([
    html.H1("📊 Dashboard Bitcoin - Projet Git"),
    html.H2(id="latest-price"),  # Le prix sera mis à jour dynamiquement
    dcc.Graph(id="price-graph"),
    html.Div([
        html.H3("🧾 Rapport du jour"),
        html.P(id="avg"),
        html.P(id="min"),
        html.P(id="max"),
    ]),
    dcc.Interval(
        id="interval-component",
        interval=60*1000,  # 60 000 ms = 1 minute
        n_intervals=0
    )
])

@app.callback(
    Output("latest-price", "children"),
    Output("price-graph", "figure"),
    Output("avg", "children"),
    Output("min", "children"),
    Output("max", "children"),
    Input("interval-component", "n_intervals")
)
def update_dashboard(n):
    df = pd.read_csv("data.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    today = pd.Timestamp.today().date()
    df_today = df[df["timestamp"].dt.date == today]

    latest_price = df_today["price"].iloc[-1]
    latest_time = df_today["timestamp"].iloc[-1].strftime("%H:%M:%S")

    daily_avg = df_today["price"].mean()
    daily_min = df_today["price"].min()
    daily_max = df_today["price"].max()

    fig = px.line(df_today, x="timestamp", y="price", title="Evolution of bitcoin price (EUR)")

    return (
        f"Dernier prix : {latest_price} EUR (à {latest_time})",
        fig,
        f"Moyenne : {daily_avg:.2f} EUR",
        f"Min : {daily_min:.2f} EUR",
        f"Max : {daily_max:.2f} EUR"
    )




if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8050)













