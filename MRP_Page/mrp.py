from dash import Dash, dcc, html, Input, Output, State, callback,dash_table as dt

import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date,datetime

today = date.today()
d4 = today.strftime("%b-%d-%Y")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

mrp_df = pd.read_csv("MRP_Page//mrp_table.csv")

layout = html.Div([

    dcc.ConfirmDialog(id='newpart-dialog',message='Message'),
	
    dcc.ConfirmDialog(id='newvend-dialog',message='Message'),

    dbc.Toast(
            [dcc.Input(id="newpart_partid", type="text", placeholder="PartID", debounce=True, style = {'height':32,'width':200,'border':'0px solid'}),
            dcc.Input(id="newpart_desc", type="text", placeholder="Description", debounce=True, style = {'height':32,'width':200, 'margin-left':10,'border':'0px solid'}),
            dcc.Dropdown(['MISCELLANEOUS','STANDARD'], id='newpart_mattype',style = {'width':200,'display':'inline-grid','margin-left':10}),
            dcc.Dropdown([''], id='newpart_vendcode',style = {'width':200,'display':'inline-grid','margin-left':10}),
            dcc.Input(id="newpart_qtyonhand", type="number", placeholder="Qty On Hand", debounce=True, style = {'height':32,'width':200, 'margin-left':20,'border':'0px solid'}),
            dcc.Input(id="newpart_price", type="text", placeholder="Price", debounce=True, style = {'height':32,'width':200, 'margin-left':10,'border':'0px solid'}),
            html.Img(id = 'newpart_submitbtn', src = 'assets/plus_icon_mini.svg',width = 30, height = 30, style = {'margin-left':20,'cursor':'pointer'}),
            ],
            id="mrp_newpart_toast",
            header="Add New Material",
            icon="info",
            dismissable=True,
            is_open=False,
			style = {'position':'absolute','width':'70%','zIndex':5,'top':230,'left':0,'background-color':'rgba(225,225,225,0.9)'},
        ),
		
	dbc.Toast(
            [dcc.Input(id="newvend_vendcode", type="text", placeholder="Code", debounce=True, style = {'height':32,'width':100,'border':'0px solid'}),
            dcc.Input(id="newvend_vendname", type="text", placeholder="Vendor Name", debounce=True, style = {'height':32,'width':200, 'margin-left':10,'border':'0px solid'}),
            html.Br(),html.Br(),
            dcc.Input(id="newvend_adrs1", type="text", placeholder="Address Line 1", debounce=True, style = {'height':32,'width':200,'border':'0px solid'}),
            dcc.Input(id="newvend_adrs2", type="text", placeholder="Address Line 2", debounce=True, style = {'height':32,'width':200, 'margin-left':10,'border':'0px solid'}),
            dcc.Input(id="newvend_adrs3", type="text", placeholder="Address Line 3", debounce=True, style = {'height':32,'width':200, 'margin-left':10,'border':'0px solid'}),
            html.Br(),html.Br(),
            dcc.Input(id="newvend_country", type="text", placeholder="Country", debounce=True, style = {'height':32,'width':200,'border':'0px solid'}),
            dcc.Input(id="newvend_city", type="text", placeholder="City", debounce=True, style = {'height':32,'width':100, 'margin-left':10,'border':'0px solid'}),
            dcc.Input(id="newvend_state", type="text", placeholder="State", debounce=True, style = {'height':32,'width':100, 'margin-left':10,'border':'0px solid'}),
            dcc.Input(id="newvend_zip", type="text", placeholder="Zip", debounce=True, style = {'height':32,'width':100, 'margin-left':10,'border':'0px solid'}),
            html.Img(id = 'newvend_submitbtn', src = 'assets/plus_icon_mini.svg',width = 30, height = 30, style = {'margin-left':20,'cursor':'pointer'}),
            ],
            id="mrp_newvend_toast",
            header="Add New Vendor",
            icon="primary",
            dismissable=True,
            is_open=False,
            style = {'position':'absolute','width':'40%','zIndex':5,'top':230,'left':200,'background-color':'rgba(225,225,225,0.9)'},
        ),	
    
    dcc.Interval(id='mrp_clock',interval=1000,n_intervals=0),
    html.Div(id = 'offmenu', className = 'sidenav', children = [
	
    html.Img(id = 'menuexitbtn', src = 'assets/exit_icon.svg',width = 35, height = 35, style = {'position':'absolute','zIndex':5,'top':20,'cursor':'pointer','right':20}),
	
    ]),

    html.Img(id = 'menubtn', src = 'assets/menu_icon.svg',width = 35, height = 35, style = {'position':'absolute','zIndex':5,'top':20,'left':10,'cursor':'pointer'}),
    html.Div(id = 'mrp-navbar',children = [html.P('MRP Manufacturing',style = {'font-size':48,'margin-left':70})],style = {'color':'white','background-color':'#193055','width': '100%','height':75}),
    html.Div(id = 'mrp-submenu', children = [
	
    html.H1(id = "mrp_clockheader", children = 'Current Time: ',style = {'position':'absolute','font-family':'sans-serif','font-weight':'bold','font-size':48,'top':90}),
    dcc.Input(id="mrp_searchbar", type="search", placeholder="Search Inventory",style = {'width':500,'position':'absolute','border-radius':5,'font-family':'sans-serif','font-size':32,'top':90,'right':90}),
    html.Img(src = 'assets/search_icon.svg',width = 50, height = 50, style = {'position':'absolute','zIndex':5,'top':90,'right':20}),
    html.Br(),
    html.Button('+ New Part', id='newpart_btn',style = {'position':'absolute','background-color':'#1D3964','border-radius':5,'color':'white','font-family':'sans-serif','font-size':32,'top':160,'left':0}),
    html.Button('+ New Vendor', id='newvend_btn',style = {'position':'absolute','background-color':'#1D3964','border-radius':5,'color':'white','font-family':'sans-serif','font-size':32,'top':160,'left':200}),
    html.Button('v Export Table', id='export_btn',style = {'position':'absolute','background-color':'#1D3964','border-radius':5,'color':'white','font-family':'sans-serif','font-size':32,'top':160,'left':450}),
	
    dcc.DatePickerRange(month_format='MMM Do, YY',end_date_placeholder_text='M/D/Y',start_date=today,style = {'position':'absolute','top':160,'right':90}),
    ],style = {'color':'white','background-color':'#BDD3F7','width': '100%','height':150}),
	
    dt.DataTable(
    id = "mrp-table",
    data=mrp_df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in mrp_df.columns],
    page_action="native",
    filter_action="native",
    filter_options={"placeholder_text": "Filter column..."},
    style_table = {'width':'100%','height':700,'maxHeight':700,'overflowX': 'auto','text-align':'left'},
    style_filter={'font-family':'sans-serif','text-align':'left','font-size':16,'backgroundColor': '#F1F1F1','border':'0px solid'},
    style_as_list_view=True,
    style_cell={'padding': '5px','font-family':'sans-serif','text-align':'left','font-size':24,'backgroundColor': 'white','border':'5px solid #9DBAE9'},
    style_header={'backgroundColor': 'white','fontWeight': 'bold','font-family':'sans-serif','text-align':'left','font-size':16},
    ),
	
    dcc.Download(id="mrp_download"),
	
	
],style = {'background-color':'#9DBAE9','height':'100%','width':'100%','position':'fixed'})

	

@callback(Output('mrp_clockheader','children'),
          Input('mrp_clock','n_intervals'),
)
def UpdateMRPClock(interval):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return 'Current Time: '+current_time



@callback(Output('newpart_vendcode','options'),
          Input('mrp_clock','interval'),
)
def UpdateVendCodes(interval):

    vend_df = pd.read_csv("MRP_Page//mrp_vendor.csv")
	
    return vend_df.VEND_CODE
	
	
	
@callback(Output('offmenu','style'),
          Output('menuexitbtn','src'),
          Output('menubtn','n_clicks'),
          Output('menuexitbtn','n_clicks'),
		  
          Input('menubtn','n_clicks'),
          Input('menuexitbtn','n_clicks'),
)
def OpenOffMenu(n_clicks,exit):
    
    if exit != None:
       return {'width':0},'assets/exit_full_icon.svg',None,None
	
    if n_clicks != None:
       if n_clicks % 2 == 1:
          return {'width':300},'assets/exit_icon.svg',n_clicks,None
       else:
          return {'width':0},'assets/exit_full_icon.svg',n_clicks,None
    else:
       return {'width':0},'assets/exit_full_icon.svg',n_clicks,None
	   
	   
	   
@callback(
          Output('newpart-dialog', 'displayed'),
          Output('newpart-dialog', 'message'),
          Output('mrp_newpart_toast','is_open'),
          Output('mrp-table','data'),
          Output('newpart_btn','n_clicks'),
          Output('newpart_submitbtn','n_clicks'),
		  
          State('newpart_partid','value'),
          State('newpart_desc','value'),
          State('newpart_mattype','value'),
          State('newpart_vendcode','value'),
          State('newpart_qtyonhand','value'),
          State('newpart_price','value'),
          State('app_user','data'),
          Input('mrp_searchbar','value'),
          Input('newpart_btn','n_clicks'),
          Input('newpart_submitbtn','n_clicks'),
)
def NewMaterialAndFilter(partid,desc,type,vend,qtyonhand,price,loginuser,searchbar,open,submit):
    
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
	
    mrp_df = pd.read_csv("MRP_Page//mrp_table.csv")
	
    mrp_log = pd.read_csv("MRP_Page//mrp_log.csv")
	
    if searchbar != None and searchbar != " ":
       mrp_filt = mrp_df[mrp_df.PART_ID.str.contains(str(searchbar)) | mrp_df.DESCRIPTION.str.contains(str(searchbar)) | mrp_df.MAT_TYPE.str.contains(str(searchbar)) | mrp_df.VENDOR_CODE.str.contains(str(searchbar)) | mrp_df.DATE_CREATED.str.contains(str(searchbar))]

       if len(mrp_filt) > 0:
          return False,'',False,mrp_filt.to_dict('records'),None,None
       else:
          return False,'',False,mrp_filt.to_dict('records'),None,None
    if open != None:
       if submit != None:
          if partid != None and desc != None and type != None and vend != None and qtyonhand != None and price != None:
             try:
                 float(price)
                 price = round(float(price),2)
             except ValueError:
                 return True,'Price is not a decimal, please enter Price as a decimal format',True,mrp_df.to_dict('records'),None,None
			 
             d = {'INDEX':[len(mrp_df)],'PART_ID':[str(partid)],'DESCRIPTION':[str(desc)],'MAT_TYPE':[str(type)],'MAT_CODE':[str(type)[0:4]],'VENDOR_CODE':[str(vend)],'QTY_ON_HAND':[int(qtyonhand)],'QTY_ALLOCATED':[0],'CURRENT_PRICE':[price],'TOTAL_PRICE':[round(int(qtyonhand)*price,2)],'DATE_CREATED':[d4]}
             w = pd.DataFrame(d)
			 
             w.to_csv("MRP_Page//mrp_table.csv", mode = "a", index = None, header = None)
			 
             d = {'INDEX':[len(mrp_log)],'USER':[str(loginuser)],'PART_ID':[str(partid)],'DESCRIPTION':[str(desc)],'MAT_TYPE':[str(type)],'MAT_CODE':[str(type)[0:4]],'VENDOR_CODE':[str(vend)],'QTY_ON_HAND':[int(qtyonhand)],'QTY_ALLOCATED':[0],'CURRENT_PRICE':[price],'TOTAL_PRICE':[round(int(qtyonhand)*price,2)],'DATE_CREATED':[d4],'ACTION':['[+]NP']}
             w = pd.DataFrame(d)
			 
             w.to_csv("MRP_Page//mrp_log.csv", mode = "a", index = None, header = None)
             mrp_df = pd.read_csv("MRP_Page//mrp_table.csv") 			 
             return False,'',True,mrp_df.to_dict('records'),None,None
          else:
             return True,'Missing Parameters, please fill out all entries to add a new Item',True,mrp_df.to_dict('records'),None,None
       else:
          return False,'',True,mrp_df.to_dict('records'),1,None
    else:
       return False,'',False,mrp_df.to_dict('records'),None,None
   

   
@callback(
          Output('newvend-dialog', 'displayed'),
          Output('newvend-dialog', 'message'),
          Output('mrp_newvend_toast','is_open'),
          Output('newvend_btn','n_clicks'),
          Output('newvend_submitbtn','n_clicks'),
		  
          State('newvend_vendcode','value'),
          State('newvend_vendname','value'),
          State('newvend_adrs1','value'),
          State('newvend_adrs2','value'),
          State('newvend_adrs3','value'),
          State('newvend_country','value'),
          State('newvend_city','value'),
          State('newvend_state','value'),
          State('newvend_zip','value'),
          State('app_user','data'),
          Input('newvend_btn','n_clicks'),
          Input('newvend_submitbtn','n_clicks'),
)
def NewVendor(vcode,vname,vadrs1,vadrs2,vadrs3,vcountry,vcity,vstate,vzip,loginuser,vbtn,submit):
    
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
	
    vend_df = pd.read_csv("MRP_Page//mrp_vendor.csv")
	
    mrp_log = pd.read_csv("MRP_Page//mrp_log.csv")
	
 

    if vbtn != None:
       if submit != None:
          if vcode != None and vname != None and vadrs1 != None and vcountry != None and vcity != None and vstate != None and vzip != None:
			 
             if vadrs2 != None:
                vadrs2 = ""
             if vadrs3 != None:
                vadrs3 = ""
			 
             d = {'INDEX':[len(mrp_log)],'USER':[str(loginuser)],'PART_ID':[""],'DESCRIPTION':[""],'MAT_TYPE':[""],'MAT_CODE':[""],'VENDOR_CODE':[str(vcode)],'QTY_ON_HAND':[""],'QTY_ALLOCATED':[""],'CURRENT_PRICE':[""],'TOTAL_PRICE':[""],'DATE_CREATED':[d4],'ACTION':['[+]NV']}
             w = pd.DataFrame(d)
			 
             w.to_csv("MRP_Page//mrp_log.csv", mode = "a", index = None, header = None)

             d = {'INDEX':[len(vend_df)],'VEND_CODE':[str(vcode)],'VENDORNAME':[str(vcode)],'ADRS1':[str(vadrs1)],'ADRS2':[str(vadrs2)],'ADRS3':[str(vadrs3)],'COUNTRY':[str(vcountry)],'CITY':[str(vcity)],'STATE':[vstate],'ZIP':[vzip],'DATE_CREATED':[d4]}
             w = pd.DataFrame(d)
			 
             w.to_csv("MRP_Page//mrp_vendor.csv", mode = "a", index = None, header = None)	
 			 
             return True,'Vendor Submitted',False,None,None
          else:
             return True,'Missing Parameters, please fill out all entries to add a new Item',True,None,None
       else:
          return False,'',True,1,None
    else:
       return False,'',False,None,None
	   
   
   
@callback(
    Output("mrp_download", "data"),
    Output("export_btn", "n_clicks"),
	
    Input("mrp-table", "filter_query"),
    Input('mrp_searchbar','value'),
    Input("export_btn", "n_clicks"),
    prevent_initial_call=True,
)
def DownloadTable(filt,searchbar,n_clicks):

    mrp_df = pd.read_csv("MRP_Page//mrp_table.csv")
    if n_clicks != None:
       if filt != None:
          filt = filt.replace('scontains','%')
          filt = filt + "&"

          collist = []
          valuelist = []
          val = ""
          for f in str(filt):
              if f == '}':
                 collist.append(val)
                 val = ""
              if f == '&':
                 valuelist.append(val)
                 val = ""			  
              if f != ' ' and f != '' and f != '&' and f != '{' and f != '}' and f != '%':
                 val += f
          for v in valuelist:
              #print(v)
              if v == '':
                 valuelist.remove(v)
       
          mrp_filt = mrp_df
          count = 0
          for c in collist:
              mrp_filt = mrp_filt[(mrp_filt[c] == str(valuelist[count]))]
              count += 1
		  	  
          return dcc.send_data_frame(mrp_filt.to_csv, "mrp_table_dwn.csv"),None
       else:
          return dcc.send_data_frame(mrp_df.to_csv, "mrp_table_dwn.csv"),None
			
			
       
       if searchbar != None and searchbar != " ":
          mrp_filt = mrp_df[mrp_df.PART_ID.str.contains(str(searchbar)) | mrp_df.DESCRIPTION.str.contains(str(searchbar)) | mrp_df.MAT_TYPE.str.contains(str(searchbar)) | mrp_df.VENDOR_CODE.str.contains(str(searchbar)) | mrp_df.DATE_CREATED.str.contains(str(searchbar))]
          return dcc.send_data_frame(mrp_filt.to_csv, "mrp_table_dwn.csv"),None
    else:
       return None,None

	
       







