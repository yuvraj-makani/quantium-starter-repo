import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the processed data
df = pd.read_csv("data/formatted_sales_data.csv")

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Sort data by date
df = df.sort_values(by="date")

# Create the Dash app
app = dash.Dash(__name__)

# Create the figure (line chart)
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time", labels={"sales": "Total Sales", "date": "Date"})

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualisation", style={'textAlign': 'center'}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
