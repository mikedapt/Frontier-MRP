from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd

layout = html.Div(children = [

    dcc.ConfirmDialog(id='login-dialog',message='Logged in'),
	
    dcc.Location(id='log_url', refresh=False),
    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
    html.H1(className = 'noblur',children = 'Welcome',style = {'font-size': 96,'text-align': 'center','color':'white','position':'relative','zIndex':2}),
    
    html.Div(className = 'grad'),
	
    html.Div(className = 'login-box', children = [
    html.H3('Login',style = {'position':'absolute','color':'white','margin-left':10,'font-size':32,'zIndex':2}),
    dcc.Input(id="login-user", type="text", debounce=True, persistence=True, persistence_type = 'session',placeholder="Enter Username",style = {'width': '90%','height':60,'zIndex':3,'font-size':24,'margin-left':10,'margin-top':100,'position':'absolute'}),
    dcc.Input(id="login-pass", type="password", debounce=True, persistence=True, persistence_type = 'session',placeholder="Enter Password",style = {'width': '90%','height':60,'zIndex':3,'font-size':24,'margin-left':10,'margin-top':200,'position':'absolute'}),
    html.Button('Login', id='login-btn',style = {'width': '91%','height':60,'zIndex':3,'font-size':24,'margin-left':10,'margin-top':300,'position':'absolute','cursor':'pointer'}),
    dcc.Checklist(id='login-remember',options = ['Remember Me'],style = {'font-size':24,'margin-left':10,'margin-top':400,'position':'absolute','cursor':'pointer'}),
    dcc.Link('New User? Register Here', href='/register',style = {'font-size':24,'text-decoration':'underline','color':'blue','text-align': 'left','position':'absolute','margin-left':10,'margin-top':450}),
    html.Div(id = 'log_refresh'),
    ]),
	
],style = {'margin-top':-80})



	

	
@callback(
    Output('login-dialog', 'displayed'),
    Output('login-dialog', 'message'),
    Output('login-btn', 'n_clicks'),
    Output('login-user', 'persistence_type'),
    Output('log_url', 'pathname'),
    Output('log_conf','data'),
    Output('log_refresh','children'),
    #Output('login-pass', 'persistence_type'),
	
    State('login-user', 'value'),
    State('login-pass', 'value'),
    State('login-remember', 'value'),
    Input('login-btn', 'n_clicks'),
    State('log_url', 'pathname'),
)
def Login(user,pwrd,rem,loginbtn,urlpath):

    log = pd.read_csv("login_cred.csv")
	
    if loginbtn != None:
       if user != None and pwrd != None:
          filt = log[log.USER == str(user)]
          log_index = 0
          if len(filt) > 0:
             for f in filt.index:
                 log_index = filt['INDEX'][f]  
					
             if str(pwrd) == log['PASSWORD'][int(log_index)]:
                if rem != None:
                   return False,'',1,'session','/mrp',1,html.Meta(httpEquiv ="refresh", content="1")
                else:
                   return False,'',1,'local','/mrp',1,html.Meta(httpEquiv ="refresh", content="1")
             else:
                return True,'Incorrect Password, Please Put a Correct Password',None,'session',urlpath,0,True
          else:
             return True,'Invalid User, Please Put an existing User or Register your Account',None,'session',urlpath,0,True
       else:
          return True,'Missing Parameters, Please fill out all Entries',None,'session',urlpath,0,True
    else:
       return False,'',None,'session',urlpath,0,True
