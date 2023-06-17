from dash import Dash, html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd


estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR] + estilos)
app.config.suppress_callback_exceptions=True

app.layout = dbc.Container([
    dcc.ConfirmDialog(message='', id='message', displayed=False),
    dbc.Col([
        dbc.Row([
            dbc.Col([dbc.Select(options=['Alimentacao', 'Entretenimento'], id='categoria')], md=2),
            dbc.Col([dbc.Input(value=0, type='number', id='valor')], md=2),
            dbc.Col([dbc.Button('Enviar', id='enviar')], md=2)
        ]),
        dbc.Row([
            dash_table.DataTable(id='dados', columns=[{'name': 'valor', 'id': 'valor'}, {'name': 'categoria', 'id': 'categoria'}])
        ], className='mt-5')
    ], md=12)
], className='mt-5')

def aux_error(message):
    return [message, True]

@app.callback(
    [Output('dados', 'data'),
     Output('message', 'message'),
     Output('message', 'displayed')],
    [Input('enviar', 'n_clicks')],
    [State('valor', 'value'),
     State('categoria', 'value'),
     State('dados', 'data')]
)

def incluir(click, valor, categoria, posicao):
    if click is None:
        raise PreventUpdate

    if valor == 0 or categoria == None:
        return [None, *aux_error('O valor não pode ser 0')]

    default_alerta_message = ['', False]

    df = [{'categoria': categoria, 'valor': valor}]
    df = pd.DataFrame(data=df)

    df_posicao = pd.DataFrame(data=posicao)

    if not df_posicao.empty:
        nova_posicao = pd.concat([df, df_posicao])
        return [nova_posicao.to_dict('records'), *default_alerta_message]
    return [df.to_dict('records'), *default_alerta_message]



if __name__ == '__main__':
    app.run(debug=True)