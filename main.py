import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 

# import and clean data 
df = pd.read_csv("2004-2017_usa_spending.csv")

# app layout - components 
app.layout = html.Div([
    html.H1("How does you state rank?", style={'text-align':'center', 'font-family': 'sans-serif'}),
    html.Div([
 dcc.Slider(id='slct_year',
    min=2005,
    max=2017,
    step=None, 
    marks={
        2005: '2005',
        2006: '2006',
        2007: '2007',
        2008: '2008',
        2009: '2009',
        2010: '2010',
        2011: '2011', 
        2012: '2012',
        2013: '2013',
        2014: '2014',
        2015: '2015',
        2016: '2016',
        2017: '2017'
    },
    value=2005    
    ),
    
     dcc.Dropdown(id='slct_fndng',
    options=[
        {"label": "Total Spending", "value": "total"},
        {"label": "Elementary and Secondary Education", "value": "elementary_and_secondary_edu"},
        {"label": "Higher Education", "value": "higher_edu"},
        {"label": "Public Welfare", "value": "public_welfare"},
        {"label": "Health and Hospital", "value": "health_and_hospitals"},
        {"label": "Highways", "value": "highways"},
        {"label": "Police", "value": "police"},
        {"label": "Other", "value": "all_other"},
        {"label": "Population", "value": "population_thousands"}],
        multi=False,
        value="total",
        style={'width': "48%"}
        ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='usa_map', figure={}) 
    ], className="row")
])

# connect using the callbacks
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='usa_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value'),
    Input(component_id='slct_fndng', component_property='value')]
)
def update_graph(year, funding):
    # option_slctd refers to value
    container = "Year: {}".format(year)

    df_copy = df.copy()
    df_year = df_copy[df_copy["year"] == year]

    
    # fig = px.choropleth(
    #     data_frame=df_year, 
    #     locationmode='USA-states',
    #     locations='status_code',
    #     scope='usa',
    #     color=funding,
    #     color_continuous_scale="Viridis",
    #     template='plotly_dark'
    # )

    fig = make_subplots(rows=1, cols=2, column_widths=[0.7, 0.3])

    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)

    fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
              row=1, col=2)

    # plotly graph objects 
    # fig = go.Figure(data=[go.Choropleth(
    #     locationmode='USA-states',
    #     locations=df_copy['state_code'],
    #     z=df_copy['police'].astype(float),
    #     colorscale='Reds',
    # )])

    # fig.update_layout(
    #     title_text = "Police Spending",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5, 
    #     geo=dict(scope='usa'),
    # )
    
    return container, fig # the outputs

# run the app 
if __name__ == "__main__":
    app.run_server(debug=True)