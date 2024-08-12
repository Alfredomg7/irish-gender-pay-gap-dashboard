from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import components as cmp
from utils import format_columns

# Load data from GitHub repository
df_filepath = 'gpg.csv'
df = pd.read_csv(df_filepath)

# Format columns for better readibility
format_columns(df)

# Create select component for filter by metric
metrics = [col for col in df.columns if 'Mean' in col or 'Median' in col]
metrics_select = cmp.create_select(metrics, id="metrics-select")

# Create plot containers
plot_style= {'height': '40vw'}
metrics_box_plot = dcc.Graph(id='metrics-box-plot', style=plot_style)
metrics_histogram = dcc.Graph(id='metrics-histogram', style=plot_style)

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define layout
app.layout = html.Div(
    [
        dbc.Container([
            dbc.Row([
                dbc.Col([html.H1('Irish Gender Pay Gap', className='display-4')], md=8, xs=12, className='my-3'),
                dbc.Col([metrics_select], sm=4, xs=12)
                ]),
            dbc.Row([
                dbc.Col(metrics_box_plot, lg=6, md=12, className='mb-3'),
                dbc.Col(metrics_histogram, lg=6, md=12, className='mb-3')
                ]),
            ], 
            fluid=True,
            className='px-4 py-2'
        ),
        html.Footer(
            [
                html.Div(
                [
                    html.A('Source Code', href='https://github.com/Alfredomg7/irish-gender-pay-gap-dashboard', target='_blank', className='link-success link-underline-opacity-0'),
                    html.Span(' | '),
                    html.A('Dataset Source', href='https://github.com/zenbuffy/irishGenderPayGap', target='_blank', className='link-success link-underline-opacity-0')
                ],
                className='text-center py-2 fs-5',
                style={
                    'position': 'fixed',
                    'bottom': '0',
                    'background-color': '#E2F2E2',
                    'border-top': '1px solid #d1d1d1',
                    'width': '100%',
                    'box-shadow': '0 -1px 5px rgba(0,0,0,0.1)',
                    'z-index': '1000'
                    }
                )
            ]
        ),
    ],
    style={'background-color': '#E2F2E2', 'min-height': '100vh'}
)

# Callbacks
@app.callback(
    Output('metrics-box-plot', 'figure'),
    Output('metrics-histogram', 'figure'),
    Input('metrics-select', 'value')
)
def update_charts(selected_metric):
    if selected_metric:
        min_year = df['Year'].min()
        max_year = df['Year'].max()

        box_plot = cmp.create_box_plot(df, selected_metric, min_year, max_year)
        histogram = cmp.create_histogram(df, selected_metric, min_year, max_year)
        return box_plot, histogram
    else:
        empty_figure = {'data': [], 'layout': {}}
        return empty_figure, empty_figure

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)