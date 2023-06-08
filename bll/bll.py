from dal.dal import Dal
import plotly.express as px

class Bll:

    def __init__(self):
        ...

    @classmethod
    def get_grafico_retornos(cls, ticker):
        preco_historico = Dal.get_retornos(ticker=ticker)
        preco_historico['Retorno'] = preco_historico['Close'].pct_change()
        preco_historico.dropna(axis=0, inplace=True)
        fig = px.line(data_frame=preco_historico, x='Date', y='Retorno', title='Retornos', template='simple_white')
        return fig

