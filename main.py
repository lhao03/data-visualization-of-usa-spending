import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
from states import state_codes, states_names, get_state, get_proper_name

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, assets_url_path='assets') 

# import data
df = pd.read_csv("2004-2017_usa_spending.csv")

df_incarceration = pd.read_csv("2013-2016_incarceration_usa.csv")

graph_theme = dict(
    layout=go.Layout(title_font=dict(family="Rockwell", size=24))
)

def make_mappings():
    list_of_labels_vals = []
    list_of_labels_vals.append({"label": "USA", "value": "USA"})
    for i in range(0, len(state_codes)):
        label_dict = {"label": states_names[i]}
        label_dict["value"] = state_codes[i]
        list_of_labels_vals.append(label_dict)
    return list_of_labels_vals

# app layout - components 
app.layout = html.Div([
    html.H1("Rate of US Spending", style={'font-weight': 'bold', 'margin':'auto', 'font-size': '50px', 'text-align':'center'}),
    html.P("Select a year and funding category. Spending is represented as dollars per capita. You can also choose to select a state to see their changes in funding over 2005 to 2017.",
        style={'background-color': 'white','margin': '20px 40px', 'text-align': 'center', 'padding': '10px', 'borderRadius': '15px', 'box-shadow': '2px 2px #888888', 'font-size':'14px'}),

    html.Div([   
    # div holding slider 
    html.Div([
        # slider for usa map
        dcc.Slider(id='slct_year', min=2005, max=2017, step=None, marks={
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
    }, value=2005),
    
    # drop down for usa map   
        dcc.Dropdown(id='slct_fndng', options=[
        {"label": "Total Spending", "value": "total"},
        {"label": "Elementary and Secondary Education", "value": "elementary_and_secondary_edu"},
        {"label": "Higher Education", "value": "higher_edu"},
        {"label": "Public Welfare", "value": "public_welfare"},
        {"label": "Health and Hospital", "value": "health_and_hospitals"},
        {"label": "Highways", "value": "highways"},
        {"label": "Police", "value": "police"},
        {"label": "Other", "value": "all_other"},
        {"label": "Population", "value": "population_thousands"}], multi=False,
        value="total", style={'width': '50%', 'margin': 'auto'}),
        
        html.Div([dcc.Graph(id='usa_map', figure={}),], style={'margin': '10px', 'background-color': '#EEE5E9', 'borderRadius': '25px'}),
        
    ]),

    # div holding graphs that are state specific 
    html.Div([
        dcc.Dropdown(id='slct_state', options=make_mappings(), value="USA", style={'margin': 'auto', 'width': '50%'}),

        dcc.Graph(id='state_figure', figure={},style={'margin-top': '10px'})], 
        style={
            'width': '95%',
            #  'align': 'right',
              'display': 'inline-block'
    }),
], style={ 'columnCount': 2}),
html.Div([
    html.H1("A look at Incarceration Rates", style={'text-align':'center'}),
    html.P("Select a year and incarceration category.",
        style={'background-color': 'white','margin': '20px 80px', 'text-align': 'center', 'padding': '10px', 'borderRadius': '15px', 'box-shadow': '2px 2px #888888', 'font-size':'14px'}),
        html.Div([
        dcc.Slider(id='slct_year_inc', min=2005, max=2017, step=None, marks={
        2013: '2013',
        2014: '2014',
        2015: '2015',
        2016: '2016'
    }, value=2013),

    dcc.Dropdown(id='slct_type_inc', options=[
        # total_correctional_pop,csrp_100k_18,csrp_100k_all,parole,comsrp_100k_18,comsrp_100k_all,local_jail_prison,irp_100k_18,irp_100k_all
        {"label": "Total correctional population", "value": "total_correctional_pop"},
        {"label": "Correctional supervision rate per 100,000 U.S. residents ages 18 or older", "value": "csrp_100k_18"},
        {"label": "Correctional supervision rate per 100,000 U.S. residents of all ages", "value": "csrp_100k_all"},
        {"label": "Number on probation or parole", "value": "parole"},
        {"label": "Community supervision rate per 100,000 U.S. residents ages 18 or older", "value": "comsrp_100k_18"},
        {"label": "Community supervision rate per 100,000 U.S. residents of all ages", "value": "comsrp_100k_all"},
        {"label": "Number in prison or local jail", "value": "local_jail_prison"},
        {"label": "Incarceration rate per 100,000 U.S. residents ages 18 or older", "value": "irp_100k_18"},
        {"label": "Incarceration rate per 100,000 U.S. residents of all ages", "value": "irp_100k_all"},
        ], multi=False,
        value="total_correctional_pop", style={ 'margin': 'auto'}),

    ], style={'columnCount': 2}),


    dcc.Graph(id='incarceration_figure', figure={}, style={'margin': '10px'}),
]),
html.Div([
    
]),
    html.P("These data come largely from the US Census Bureau’s Census of Governments and Annual Survey of State and Local Government Finances; additional data are from the US Bureau of Economic Analysis and the US Bureau of Labor Statistics.",
    id='p-info', style={'background-color': 'white', 'margin': '25px', 'text-align': 'center', 'padding': '10px', 'font-size': '10px', 'text-align': 'left', 'borderRadius': '15px', 'box-shadow': '2px 2px #888888'}),
], style={})


# connect using the callbacks
@app.callback(
    [Output(component_id='usa_map', component_property='figure'),
    Output(component_id='state_figure', component_property='figure'),
    Output(component_id='incarceration_figure', component_property='figure')],
    [Input(component_id='slct_year', component_property='value'),
    Input(component_id='slct_fndng', component_property='value'),
    Input(component_id='slct_state', component_property='value'),
    Input(component_id='slct_year_inc', component_property='value'),
    Input(component_id='slct_type_inc', component_property='value')
    ]
)
def update_graph(year, funding, state, year_inc, type_inc):
    # option_slctd refers to value

    # data manipulation for the USA map 
    df_copy = df.copy()
    df_year = df_copy[df_copy["year"] == year]

    # year by year     
    fig_usa = px.choropleth(
        data_frame=df_year, 
        locationmode='USA-states',
        locations='status_code',
        scope='usa',
        color=funding,
        color_continuous_scale="Viridis",
        template='plotly_white',
        hover_data=[df_year['region']],
    )

    # data manipulation for the state plots 
    fig_state = ''
    if state == "USA": 
        # box whiskter plot 
        fig_state = px.box(df_year, y=funding, points='all', template='plotly_white', hover_data=[df_year['region']], title="{funding} per state.".format(funding=get_proper_name(funding)))
        fig_state.update_traces(quartilemethod="exclusive") 
    else: 
        # specific state or compare all of the states by average
        df_state = df_copy[df_copy['status_code'] == state]
        print(df_state)
        fig_state= px.line(df_state,template='plotly_white',x="year", y=funding, title="{funding} for {state} over 2005 - 2017".format(funding=get_proper_name(funding), state=get_state(state)))

    # data for incarceration map 
    df_incarceration_copy = df_incarceration.copy()
    df_year_inc = df_incarceration_copy[df_incarceration_copy["year"] == year_inc]
    
    # data manipulation for the incarceration fig 
    fig_incarceration = px.choropleth(
        data_frame=df_year_inc, 
        locationmode='USA-states',
        locations='status_code',
        scope='usa',
        color=type_inc,
        color_continuous_scale="Viridis",
        template='plotly_white',
        hover_data=[df_year_inc['region']],
    )

    return [fig_usa, fig_state, fig_incarceration] # the outputs

# run the app 
if __name__ == "__main__":
    app.run_server(debug=True)