from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR] + estilos)
app.config.suppress_callback_exceptions=True

from apps.login.layout import get_login
from apps.dash_renda.layout import get_layout
from route import *
from apps.dash_renda.callbacks import *

dados = pd.read_csv('db/dados.csv')
estados = pd.read_csv('db/estado.csv')


app.layout = html.Div([
    dcc.Store(id='dados', data=dados.to_dict(orient='records')),
    dcc.Location(id='url', refresh=False),
    html.Div(children=[], id='conteudo')]
)


if __name__ == '__main__':
    app.run(debug=True)