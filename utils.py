import re

def camel_to_title(camel_str):
    """
    Convert camel case string to title case
    """
    title_str = re.sub(r'(?<!^)(?=[A-Z])', ' ', camel_str)
    title_str = title_str.title()
    return title_str

def format_columns(df):
    """
    Format DataFrame column names to title case with custom formatting.
    """
    formatted_columns = {}
    for col in df.columns:
        title_case = camel_to_title(col)

        if 'PT' in col:
            title_case = title_case.replace('P T', 'Part-Time')
        elif 'Temp' in col:
            title_case = title_case.replace('Temp', 'Temporary Contract')

        formatted_columns[col] = title_case
    
    df.rename(columns=formatted_columns, inplace=True)

def update_plot_layout(plot, selected_metric, axis='y'):
    """
    Update the layout of the plot based on axis orientation.

    Parameters:
    plot: plotly.graph_objects.Figure or plotly.express.Figure
        The plot to be updated.
    selected_metric: str
        The name of the selected metric.
    axis: str
        The axis on which the metric is plotted ('x' or 'y').
    """
    if axis == 'y':
        plot.update_layout(
            paper_bgcolor='#D1E7D1',
            plot_bgcolor='#D1E7D1',
            title={
                
                'x': 0.5,
            },
            xaxis=dict(
                title_text='',
                title_font_size=16,
                tickfont=dict(size=14),
                showgrid=False,
                zeroline=False,
            ),
            yaxis=dict(
                title_text=f'{selected_metric} (difference in %)',
                ticksuffix='%',
                title_font=dict(size=16),
                tickfont=dict(size=14),
                showgrid=False,
                zeroline=False,
            ),
            margin=dict(l=40, r=20, t=40, b=40),
            legend=dict(
                title='',
                font=dict(size=14)
            )
        )
    elif axis == 'x':
        plot.update_layout(
            paper_bgcolor='#D1E7D1',
            plot_bgcolor='#D1E7D1',
            title={
                'x': 0.5,
            },
            xaxis=dict(
                title_text=f'{selected_metric} (difference in %)',
                ticksuffix='%',
                title_font=dict(size=14),
                tickfont=dict(size=14),
                showgrid=False,
                zeroline=False,
            ),
            yaxis=dict(
                title_text='Frequency',
                title_font=dict(size=14),
                tickfont=dict(size=14),
                showgrid=False,
                zeroline=False,
            ),
            margin=dict(l=40, r=20, t=40, b=40),
            legend=dict(
                title='',
                font=dict(size=14)
            )
        )


