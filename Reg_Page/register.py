from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd

layout = html.Div(children = [

    dcc.ConfirmDialog(id='reg-dialog',message='New User Created!'),
    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
    html.H1(className = 'noblur',children = 'Welcome',style = {'font-size': 96,'text-align': 'center','color':'white','position':'relative','zIndex':2}),
	
	html.Div(className = 'grad'),
	
    html.Div(className = 'reg-box', children = [
    html.H3('Register Here',style = {'position':'absolute','color':'white','margin-left':10,'font-size':32,'zIndex':2}),
    dcc.Input(id="reg-user", type="text", debounce=True, placeholder="Username",style = {'width': '90%','height':60,'zIndex':3,'font-size':24,'margin-left':10,'margin-top':100,'position':'absolute'}),
    dcc.Input(id="reg-pass", type="password", debounce=True, placeholder="Password",style = {'width': '90%','height':60,'zIndex':3,'font-size':24,'margin-left':10,'margin-top':200,'position':'absolute'}),
    dcc.Input(id="reg-conf", type="password", debounce=True, placeholder="Confirm Password",style = {'width': '90%','height':60,'zIndex':3,'font-size':24,'margin-left':10,'margin-top':300,'position':'absolute'}),
    html.Button('Register User', id='reg-btn',style = {'width': '91%','height':60,'zIndex':3,'font-size':24,'margin-left':10,'margin-top':400,'position':'absolute','cursor':'pointer'}),
    dcc.Link('Back to Login', href='/login',style = {'font-size':24,'text-decoration':'underline','color':'blue','text-align': 'left','position':'absolute','margin-left':10,'margin-top':500}),
    ]),
	
    dcc.Dropdown(
        {f'Page 2 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
        id='page-2-dropdown'
    ),
    html.Div(id='page-2-display-value'),
    dcc.Link('Go to Register', href='/register'),
    html.Br(),
    dcc.Link('Go to MRP', href='/mrp'),
],style = {'margin-top':-80})


@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'
	
	
	
	
	
@callback(
    Output('reg-dialog', 'displayed'),
    Output('reg-dialog', 'message'),
    Output('reg-btn', 'n_clicks'),
	
    State('reg-user', 'value'),
    State('reg-pass', 'value'),
    State('reg-conf', 'value'),
    Input('reg-btn', 'n_clicks'),
)
def RegisterUser(user,pwrd,conf,regbtn):

    log = pd.read_csv("login_cred.csv")

    if regbtn != None:
       if user != None and pwrd != None and conf != None:
          if str(pwrd) == str(conf):
             d = {'INDEX':[len(log)],'USER':[str(user)],'PASSWORD':[str(pwrd)]}
             w = pd.DataFrame(d)
			 
             w.to_csv("login_cred.csv", mode = "a", index = None, header = None)
			 
             return True,'User '+str(user)+' Created!',None
          else:
             return True,'Passwords do not match, Please Enter the same password for both Entries',None
       else:
          return True,'Missing Parameters, Please fill out all Entries',None
    else:
       return False,'',None	