import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Initial data load
df = pd.read_csv("data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Dash app setup
app = Dash(__name__)
server = app.server  # Required for gunicorn
app.title = "Bitcoin Dashboard"

# Layout with pastel Bitcoin-style theme
app.layout = html.Div(style={
    "fontFamily": "'Lato', sans-serif",
    "backgroundColor": "#fdf6f0",
    "padding": "20px",
    "color": "#333"
}, children=[
    html.Div("📊 Bitcoin Dashboard - Projet Git", style={
        "backgroundColor": "#f7931a",  # Soft Bitcoin orange
        "color": "white",
        "padding": "20px",
        "borderRadius": "12px",
        "textAlign": "center",
        "fontSize": "32px",
        "fontWeight": "bold",
        "marginBottom": "30px"
    }),

    html.H2(id="latest-price", style={
        "textAlign": "center",
        "fontSize": "26px",
        "marginBottom": "30px"
    }),

    dcc.Graph(id="price-graph"),

    html.Div([
        html.H3("Rapport du jour", style={"color": "#f7931a"}),
        html.P(id="avg"),
        html.P(id="min"),
        html.P(id="max"),
    ], style={
        "backgroundColor": "#fff9f3",
        "padding": "20px",
        "border": "1px solid #f5d7b0",
        "borderRadius": "10px",
        "marginTop": "30px"
    }),

    html.Footer("Projet scraping en binôme - 2025", style={
        "textAlign": "center",
        "marginTop": "40px",
        "color": "#999",
        "fontSize": "14px"
    }),

    dcc.Interval(
        id="interval-component",
        interval=60 * 1000,  # 1 minute
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
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    today = pd.Timestamp.today().date()
    df_today = df[df["timestamp"].dt.date == today]

    if df_today.empty:
        return "No data available yet.", {}, "", "", ""

    latest_price = df_today["price"].iloc[-1]
    latest_time = df_today["timestamp"].iloc[-1].strftime("%H:%M:%S")

    daily_avg = df_today["price"].mean()
    daily_min = df_today["price"].min()
    daily_max = df_today["price"].max()

    fig = px.line(
        df_today, x="timestamp", y="price",
        title="Évolution du prix du Bitcoin aujourd’hui (€)",
        template="plotly_white",
        markers=True
    )

    return (
        f"Dernier prix : {latest_price:.2f} EUR (à {latest_time})",
        fig,
        f"Moyenne : {daily_avg:.2f} EUR",
        f"Min : {daily_min:.2f} EUR",
        f"Max : {daily_max:.2f} EUR"
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)












