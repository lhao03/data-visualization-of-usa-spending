import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# import and clean data 
df = pd.read_csv("intro_bees.csv")

df = df.groupby(['State','ANSI','Affected by','Year','state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

# app layout - components 
app.layout = html.Div([
    html.H1("Web app with Dash", style={'text-align':'center'}),
    dcc.Dropdown(id='slct_year',
    options=[
        {"label": "2015", "value": 2015},
        {"label": "2016", "value": 2016},
        {"label": "2017", "value": 2017},
        {"label": "2018", "value": 2018}],
        multi=False,
        value=2015,
        style={'width': "48%"}
        ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})    
])

# connect using the callbacks
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    # option_slctd refers to value
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    df_copy = df.copy()
    df_year = df_copy[df_copy["Year"] == option_slctd]
    df_varr = df_year[df_year["Affected by"] == "Varroa_mites"]

    # fig = px.choropleth(
    #     data_frame=df_varr, 
    #     locationmode='USA-states',
    #     locations='state_code',
    #     scope='usa',
    #     color='Pct of Colonies Impacted',
    #     hover_data=['State','Pct of Colonies Impacted'],
    #     color_continuous_scale=px.colors.sequential.YlOrRd,
    #     labels={'Pct of Colonies Impacted': '%\ of Bee Colonies'},
    #     template='plotly_dark'
    # )

    # plotly graph objects 
    fig = go.Figure(data=[go.Choropleth(
        locationmode='USA-states',
        locations=df_copy['state_code'],
        z=df_copy['Pct of Colonies Impacted'].astype(float),
        colorscale='Reds',
    )])

    fig.update_layout(
        title_text = "Bees",
        title_xanchor="center",
        title_font=dict(size=24),
        title_x=0.5, 
        geo=dict(scope='usa'),
    )
    
    return container, fig # the outputs

# run the app 
# if __name__ == "__main__":
#     app.run_server(debug=True)