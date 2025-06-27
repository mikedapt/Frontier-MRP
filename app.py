from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc
import pandas as pd

from Login_Page import login
from Reg_Page import register
from MRP_Page import mrp

app = Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
	
	dbc.Toast(
            [html.P("Press again to disable", className="mb-0")],
            id="toast-alerts",
            header="This is the header",
            icon="danger",
            dismissable=True,
            is_open=False,
			style = {'position':'absolute','zIndex':5,'top':50,'right':150},
        ),
	
	dbc.Toast(
            [html.P("This is the content of the toast", className="mb-0")],
            id="toast-accnt",
            header="This is the header",
            icon="primary",
            dismissable=True,
            is_open=False,
			style = {'position':'absolute','zIndex':5,'top':50,'right':100},
        ),
	
    html.Img(id = 'app_help',src = 'assets/help_icon.svg',width = 35, height = 35, style = {'position':'absolute','zIndex':5,'top':20,'right':50,'cursor':'pointer','zIndex':5}),
    html.Img(id = 'app_profile',src = 'assets/user_icon.svg',width = 35, height = 35, style = {'position':'absolute','zIndex':5,'top':20,'right':100,'cursor':'pointer','zIndex':5}),
    html.Img(id = 'app_alerts',src = 'assets/notify_icon.svg',width = 35, height = 35, style = {'position':'absolute','zIndex':5,'top':20,'right':150,'cursor':'pointer','zIndex':5}),
    html.Div(id='page-content'),
    dcc.Store(id='log_conf', storage_type='session', data = 0),
    dcc.Store(id='app_user', storage_type='session', data = ''),
	
])

@callback(Output('app_user', 'data'),		  
          Input('login-user','value'),
)		
def LogUser(value):

    return value


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'),
              Input('log_conf','data'),
)
def display_page(pathname,log):
    if pathname == '/login':
        return login.layout
    elif pathname == '/register':
        return register.layout
    elif pathname == '/mrp' and log == 1:
        return mrp.layout
    else:
        return login.layout
		

			
@callback(Output('toast-accnt', 'is_open'),
          Output('toast-accnt', 'header'),
		  
          Input('app_profile','n_clicks'),
)		
def ViewProfile(n_clicks):

    if n_clicks != None:
       return True,"Profile"
    else:
       return False,""
	   
		
		
@callback(Output('toast-alerts', 'is_open'),
          Output('toast-alerts', 'header'),
          Output('app_alerts','src'),
		  
          Input('app_alerts','n_clicks'),
)		
def ToggleAlerts(n_clicks):

    if n_clicks != None:
       if n_clicks % 2 == 0:
          return True,"Alerts Enabled",'assets/notify_full_icon.svg'
       else:
          return False,"",'assets/notify_icon.svg'
    else:
       return False,"",'assets/notify_icon.svg'
	   


if __name__ == '__main__':
    app.run(debug=True)