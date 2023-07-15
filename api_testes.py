import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
#informacoes_bolsa = pd.read_csv('dados/dados_empresas_mercado.csv')

apple_df = pdr.get_data_alphavantage()
apple_df.head()

exit()
tickers_bolsa['ticker'] = tickers_bolsa['Código'].apply(lambda x: f'{x}.SA')

print(tickers_bolsa)

tickers_list = tickers_bolsa['ticker'].tolist()
dados_empreas = []

for ticker in tickers_list:
    try:
        ticker_info = yf.Ticker(ticker).info
        if ticker_info:
            dados_empreas.append(ticker_info)
    except Exception as e:
        print('Erro ao capturar dados do ticker: ', ticker)


dados_empresas_mercado = pd.DataFrame(data=dados_empreas)
dados_empresas_mercado.to_csv('dados/dados_empresas_mercado.csv')

