import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

data = pd.read_csv('data/formatted_sales_data.csv')

# Sort by date
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values('date')

# Group sales by date
daily_sales = data.groupby('date')['sales'].sum().reset_index()

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Over Time', style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            daily_sales,
            x='date',
            y='sales',
            title='Daily Sales of Pink Morsels',
            labels={'date': 'Date', 'sales': 'Sales ($)'}
        )
    )
])


if __name__ == '__main__':
    app.run(debug=True)
