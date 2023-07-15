from main import app
from dash import Output, State, Input
from apps.login.layout import get_login
from apps.dash_renda.layout import get_layout as get_renda_laytout
@app.callback(
    [Output('conteudo', 'children', allow_duplicate=True)],
    [Input('url', 'pathname')],
    prevent_initial_call=True
)

def navigation(pathname):
    if pathname == '/' or pathname == '/login':
        return [get_login()]
    elif pathname == '/home' or pathname == '/renda':
        return [get_renda_laytout()]