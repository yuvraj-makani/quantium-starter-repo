import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load the processed data
df = pd.read_csv("data/formatted_sales_data.csv")

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Sort data by date
df = df.sort_values(by="date")

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualisation", style={'textAlign': 'center', 'color': '#FF5733'}),

    html.Label("Select a Region:", style={'fontSize': '18px', 'fontWeight': 'bold'}),
    
    dcc.RadioItems(
        id="region-filter",
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        labelStyle={'display': 'block', 'margin': '5px'}
    ),

    dcc.Graph(id="sales-line-chart"),

], style={'width': '50%', 'margin': 'auto', 'padding': '20px', 'fontFamily': 'Arial, sans-serif'})

# Callback to update the chart based on selected region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df if selected_region == "all" else df[df["region"] == selected_region]
    
    fig = px.line(
        filtered_df, x="date", y="sales",
        title=f"Pink Morsel Sales in {selected_region.capitalize()} Region",
        labels={"sales": "Total Sales", "date": "Date"}
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
