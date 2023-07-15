from main import app
from dash import Output, Input, State
from dash.exceptions import PreventUpdate
from bll.bll import Bll
from dal.dal import Dal


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

