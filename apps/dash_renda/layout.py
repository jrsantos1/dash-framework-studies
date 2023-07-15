from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc
import pandas as pd

estados = pd.read_csv('db/estado.csv', delimiter='\t')
estados = [{'value': r['UF'], 'label': r['descricao']} for _,r in estados.iterrows()]
def get_graph_pattern(size, id, padding: str = "10px"):
    return dbc.Col(dbc.Card(dcc.Graph(id=id, figure=px.bar(template='simple_white'), style={"height": "auto", "padding": padding}, className='w-100 h-100 shadow'), style={"height": "100%"}), width=size)
def get_layout():
    return html.Div([
        dbc.Navbar([
            dbc.NavLink(dbc.NavbarBrand(children='DashBoard Renda', className='text-light')),
            dbc.NavLink(dbc.NavItem(children='Home', className='text-light'))]
            , className='bg-dark', style={'heigth': '20%'}),
        dbc.Container([
        dbc.Row([
            dbc.Col(md=2),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Label('Estado'),
                        dcc.Dropdown(options=estados, multi=True, id='drop_estado_id')], md=6),
                    dbc.Col([
                        html.Label('Faixa Anos de Estudo'),
                        dcc.Slider(1, 20, 1, value=1)
                    ], md=6),
                ], className='w-100 d-flex mt-2'),

                dbc.Row([
                    get_graph_pattern(4, 'graph_1'),
                    get_graph_pattern(8, 'graph_2')
                ], style={'height': '30vh'}, id='helpme', className='mt-5'),
                dbc.Row([
                    get_graph_pattern(4, 'graph_3'),
                    get_graph_pattern(4, 'graph_4'),
                    get_graph_pattern(4, 'graph_5')
                ], className='w-100 d-flex mt-5', style={'height': '40vh'})
            ],md=10, style={'height': 'auto'})
        ])]
    , style={'height': '80%'}, fluid=True)], className='w-100', style={'height': '100vh'})