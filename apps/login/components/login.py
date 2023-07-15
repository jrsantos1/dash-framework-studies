from dash import dcc, html
import dash_bootstrap_components as dbc


login = dbc.Container(children=[
  html.Div(
      children=[
          html.Div([
              dbc.Container([
                html.H4('Login', className='text-center mt-2'),
                  html.Div([
                    html.Label(['Usuário']),
                    dbc.Input(id='login_user', required=True),
                    html.Label(['Senha']),
                    dbc.Input(id='pass_user', type='password', required=True),
                      dbc.NavLink(children='Logar', id='btn_login', href='/home',className='w-100 mt-3')
                  ])]
              ),
          ], className='w-25 h-50 bg-danger mt-5'
          , style={'opacity': '0.75', 'border-radius': '5px'})
      ],
      className='d-flex w-100 bg-secondary justify-content-center',
      style={'height': '100vh'}
  )

], fluid=True)
