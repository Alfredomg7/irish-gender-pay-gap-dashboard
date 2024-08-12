from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
from utils import update_plot_layout

year_colors = ['#4BC0D9', '#107E7D']

def create_select(options, id):
    """
    Create a select bootstrap component

    --------
    Parameters:
    options: list
        list of options to select
    id: string
        unique identifier for component

    --------
    Returns:
    select_menu: dbc.CardBody
        The select menu component
    """
    select_menu = dbc.CardBody([
        html.H4('Select Metric', className='card-title mb-2'),
        dbc.Select(
            id=id,
            options=options,
            value=options[1]
        )
    ], className='my-3'
    )

    return select_menu
    
def create_box_plot(df, selected_metric, min_year, max_year):
    """
    Create a box plot for the selected metric

    ----------
    Parameters:
    df: pd.DataFrame
        Dataframe containing the data
    selected_metric: str
        Name of the selected metric
    min_year: int
        Minimum year in the dataset
    max_year: int
        Maximum year in the dataset

    ----------
    Returns:
    box_plot: dcc.Graph
        Box plot for the selected metric
    """

    box_plot = px.box(df,
                      x='Year',
                      y=selected_metric,
                      color='Year',
                      color_discrete_sequence=year_colors,
                      title=f'{selected_metric} Box Plot {min_year}-{max_year}',
                    )
    update_plot_layout(box_plot, selected_metric, axis='y')
    return box_plot

def create_histogram(df, selected_metric, min_year, max_year):
    """
    Create a histogram for the selected metric

    ----------
    Parameters:
    df: pd.DataFrame
        Dataframe containing the data
    selected_metric: str
        Name of the selected metric
    min_year: int
        Minimum year in the dataset
    max_year: int
        Maximum year in the dataset
    
    ----------
    Returns:
    histogram: dcc.Graph
        Histogram for the selected metric
    """
    histogram = px.histogram(df,
                             x=selected_metric,
                             color='Year',
                             color_discrete_sequence=year_colors,
                             opacity=0.5,
                             title=f'{selected_metric} Histogram {min_year}-{max_year}',
                            )
    update_plot_layout(histogram, selected_metric, axis='x')
    return histogram