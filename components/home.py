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
    dash_table.DataTable(data=empresas.to_dict('records'), columns=[{'name': i, 'id': i} for i in empresas.columns],
                         filter_action='native',
                         style_header={
                             'backgroundColor': 'pink',
                             'fontWeight': 'bold'
                         })
    ], className='w-100 mt-3 shadow-lg')
], fluid=True, className='bg-light')