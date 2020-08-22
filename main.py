import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# import and clean data 
df = pd.read_csv("2004-2017_usa_spending.csv")

# app layout - components 
app.layout = html.Div([
    html.H1("How does you state rank?", style={'text-align':'center'}),
    # dcc.Dropdown(id='slct_year',
    # options=[
    #     {"label": "2005", "value": 2005},
    #     {"label": "2006", "value": 2006},
    #     {"label": "2007", "value": 2007},
    #     {"label": "2008", "value": 2008},
    #     {"label": "2009", "value": 2009},
    #     {"label": "2010", "value": 2010},
    #     {"label": "2011", "value": 2011},
    #     {"label": "2012", "value": 2012},
    #     {"label": "2013", "value": 2013},
    #     {"label": "2014", "value": 2014},
    #     {"label": "2015", "value": 2015},
    #     {"label": "2016", "value": 2014},
    #     {"label": "2017", "value": 2017},],
    #     multi=False,
    #     value=2015,
    #     style={'width': "48%"}
    #     ),
    
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

    fig = px.choropleth(
        data_frame=df_year, 
        locationmode='USA-states',
        locations='status_code',
        scope='usa',
        color=funding,
        color_continuous_scale="Viridis",
        template='plotly_dark'
    )

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