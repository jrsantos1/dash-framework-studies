import pandas as pd
from config import Config
import yfinance as yf
import datetime
from datetime import timedelta

class Dal:

    def __init__(self):
        ...
    @classmethod
    def get_empresas(self):
        dados = pd.read_csv(f'{Config.get_root_path()}/dados/dados_empresas_mercado.csv')
        return dados[['longName', 'sector', 'symbol', 'quoteType', 'beta']]

    @classmethod
    def get_retornos(cls, ticker):
        end = datetime.datetime.now()
        start = end - timedelta(days=120)
        retornos = yf.Ticker(ticker=ticker).history(period="6mo")
        retornos.reset_index(inplace=True)
        return retornos[['Date', 'Close']]

    @classmethod
    def get_dados_empresa(cls, ticker) -> pd.DataFrame:
        info = yf.Ticker(ticker=ticker).info
        dados = pd.DataFrame(data=info)
        dados.to_excel('dados_empresa.xlsx')
        dados = dados.drop_duplicates(subset='symbol')
        return dados.to_dict('records')[0]

    @classmethod
    def get_lista_empresas(cls):
        dados = pd.read_csv(f'{Config.get_root_path()}/dados/dados_empresas_mercado.csv')
        dados['customName'] = dados.apply(lambda x: f"{x['longName']} - {x['symbol']}", axis=1)
        dados = dados.rename({'customName': 'label', 'symbol': 'value'}, axis=1)
        return dados[['label', 'value']].to_dict('records')

