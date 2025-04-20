import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

data = pd.read_csv('data/formatted_sales_data.csv')

# Sort by date
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values('date')

# Create the Dash app
app = dash.Dash(__name__)

app.title = "Pink Morsel Sales Dashboard"

app.layout = html.Div([
    html.H1("Pink Morsel Sales Over Time", id='main-header'),

    html.Div([
        html.Label("Select a Region:"),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            labelStyle={'display': 'inline-block'},
            className='radio-items'
        ),
    ], style={'marginBottom': '30px'}),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'].str.lower() == selected_region]

    # Group sales by date
    daily_sales = filtered_data.groupby('date')['sales'].sum().reset_index()

    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=f'Daily Sales in {selected_region.capitalize()} Region' if selected_region != 'all' else 'Daily Sales in All Regions',
        labels={'date': 'Date', 'sales': 'Sales ($)'}
    )

    fig.update_layout(
        plot_bgcolor='#fffdfd',
        paper_bgcolor='#fffdfd',
        title_font_color='#c2185b',
        font_color='#4b2e2e',
        hovermode='x'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
