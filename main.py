from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dal.dal import Dal
from bll.bll import Bll
import plotly.express as px

estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR] + estilos)
app.config.suppress_callback_exceptions=True

from components import login, home, detalhamento


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(children=[], id='page-content')]
)

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)

def navigation(pathname):
    if pathname == '/' or pathname == '/login':
        return login.layout
    elif pathname == '/home':
        return home.layout
    elif pathname == '/detalhamento':
        return detalhamento.layout

@app.callback(
    Output('url', 'pathname'),
    Input('btn_login', 'n_clicks')
)

def logar(click):
    if click is None:
        raise PreventUpdate
    return '/home'

@app.callback(
    [Output('detalhamento_nome_empresa', 'children'),
     Output('detalhamento_cotacao', 'children'),
    Output('detalhamento_volume', 'children'),
    Output('detalhamento_nota_risco', 'children'),
    Output('detalhamento_margem_operacional', 'children'),
    Output('detalhamento_sobre', 'children'),
    Output('detalhamento_grafico_retornos', 'figure'),
     ],
    Input('btn_pesquisar_dados_empresa', 'n_clicks'),
    State('detalhamento_ticker_selecionado', 'value')
)

def pesquisar_dados_ticker(click, ticker):
    if click is None:
        raise PreventUpdate

    dados_empresa = Dal.get_dados_empresa(ticker=ticker)
    nome = dados_empresa.get('longName')
    cotacao = dados_empresa.get('regularMarketPreviousClose')
    volume = dados_empresa.get('volume')
    nota_de_risco = dados_empresa.get('overallRisk')
    sobre_a_empresa = dados_empresa.get('longBusinessSummary')
    margem_operacional = dados_empresa.get('operatingMargins')
    margem_operacional = '{:.2%}'.format(margem_operacional)

    fig = Bll.get_grafico_retornos(ticker=ticker)

    return nome, cotacao, volume, nota_de_risco, margem_operacional,sobre_a_empresa, fig


if __name__ == '__main__':
    app.run(debug=True)