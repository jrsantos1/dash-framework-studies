from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from dal.dal import Dal


empresas = Dal.get_empresas()

layout = dbc.Container(children=[

    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink(children='Empresas', active=True)),
                dbc.NavItem(dbc.NavLink(children='Comparar', active=True)),
                dbc.NavItem(dbc.NavLink(children='Índices', active=True))
            ])
        ], md=12, className='bg-secondary')
    ], className='w-100'),

    dbc.Row([
        dbc.Col(
            dcc.Dropdown(options=Dal.get_lista_empresas(), id='detalhamento_ticker_selecionado')
        ,md=10),
        dbc.Col(
            dbc.Button(children='Pesquisar', id='btn_pesquisar_dados_empresa')
        ,md=2)
    ],className='mt-3 mb-3'),

    dbc.Row(
        html.H3('', id='detalhamento_nome_empresa')
    , className='mt-3'),

    dbc.Row([
        dbc.Col(
            [
            dbc.Card(
                [
                    dbc.CardBody(children=[
                        html.H2('0', id='detalhamento_cotacao')
                    ], className='text-center'),
                    dbc.CardFooter('Cotação', style={'fontSize': '0.75rem', 'backgroundColor': '#B31312', 'color': 'white','opacity': '0.75'})
                ]
                , className='shadow-lg', style={'fontSize': '0.75rem', 'backgroundColor': '#212A3E', 'color': 'white'})
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardBody(children=[
                            html.H2('0', id='detalhamento_volume')
                        ], className='text-center'),
                        dbc.CardFooter('Volume',
                                       style={'fontSize': '0.75rem', 'backgroundColor': '#B31312', 'color': 'white',
                                              'opacity': '0.75'})
                    ]
                    , className='shadow-lg',
                    style={'fontSize': '0.75rem', 'backgroundColor': '#212A3E', 'color': 'white'})
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardBody(children=[
                            html.H2('0', id='detalhamento_nota_risco')
                        ], className='text-center'),
                        dbc.CardFooter('Nota de Risco',
                                       style={'fontSize': '0.75rem', 'backgroundColor': '#B31312', 'color': 'white',
                                              'opacity': '0.75'})
                    ]
                    , className='shadow-lg',
                    style={'fontSize': '0.75rem', 'backgroundColor': '#212A3E', 'color': 'white'})
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardBody(children=[
                            html.H2('0', id='detalhamento_margem_operacional')
                        ], className='text-center'),
                        dbc.CardFooter('Margem Operacional',
                                       style={'fontSize': '0.75rem', 'backgroundColor': '#B31312', 'color': 'white',
                                              'opacity': '0.75'})
                    ]
                    , className='shadow-lg',
                    style={'fontSize': '0.75rem', 'backgroundColor': '#212A3E', 'color': 'white'})
            ]
        ),
    ], className='mt-5'),

    dbc.Row([
        dbc.Col(
            dbc.Tabs([
                dbc.Tab(label='Retornos Históricos', children=[
                    dcc.Graph(id='detalhamento_grafico_retornos')
                ]),
                dbc.Tab(label='Sobre a Empresa', children=[
                    dbc.Container(
                        html.Div(
                            html.P('', id='detalhamento_sobre')
                        , className='mt-5')
                    ,fluid=True)
                ])]
            )
        ,md=12)
    ], className='w-100 mt-5')



], fluid=True, className='bg-light')