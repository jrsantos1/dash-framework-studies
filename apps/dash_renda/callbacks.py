from dash import Input, Output, State
from main import app
import pandas as pd
import plotly.express as px
@app.callback(
    [Output('graph_2', 'figure'),
    Output('graph_1', 'figure')],
    Input('drop_estado_id', 'value')
)

def dist_renda(estado):
    dados = pd.read_csv('db/dados.csv')
    if estado:
        estados = [int(i) for i in estado]
        dados = dados[dados['UF'].isin(estados)]
    dados_renda = dados[['Anos de Estudo', 'Renda', 'Altura']].groupby(by=['Anos de Estudo'], as_index=False).mean()

    if True:
        cor_dict = {0: 'Indígena',
               2: 'Branca',
               4: 'Preta',
               6: 'Amarela',
               8: 'Parda',
               9: 'Sem declaração'}

        def transform_color(cor):
            return cor_dict[cor]

        dados['Cor'].apply(lambda x: 1)
        dados_Cor = dados[['Cor', 'Renda']].groupby(by='Cor', as_index=False).count()
        fig_color = px.pie(data_frame=dados_Cor,  values='Renda', names='Cor')


    fig_renda = px.bar(data_frame=dados_renda, template='simple_white', x='Anos de Estudo', y='Renda', title='Renda Média', color_discrete_sequence=px.colors.sequential.RdBu)
    return fig_renda, fig_color