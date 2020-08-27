import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
################################################################ Step 1. Launch the application
#app = dash.Dash()
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
############################################################### Step 2. Import the dataset and clean it
#########first bar chart 
my_sheet1 = 'passage aux urgencesligne' # change it to your sheet name
df = pd.read_excel("C:\\Users\\Ayachi\\Desktop\\projet dataviz\\data.xlsx", sheet_name = my_sheet1)
# convertire chaque ligne en liste 
l=[]
years=[2015,2016,2017]
l1=[]
l2=[]
l3=[]
ltot=[]
l=df.values.tolist()
l1=l[1]
l2=l[2]
l3=l[3]
ltot=l[4]
del l1[0]
del l1[3]
del l1[3]
del l2[0]
del l2[3]
del l2[3]
del l3[0]
del l3[3]
del l3[3]
del ltot[0]
del ltot[3]
del ltot[3]
#new dataset for bars 
dfnew = pd.DataFrame(list(zip(years,l1, l2,l3,ltot)), columns =['years','Premiere ligne', 'Deuxieme ligne', 'Troisieme ligne','Total']) 
opts =['tous les lignes','première ligne','deuxième ligne','troisième ligne', 'Total']
######################     sunburt data frame 
my_sheet2 = '3lignegouver' # change it to your sheet name
dfsunburt = pd.read_excel("C:\\Users\\Ayachi\\Desktop\\projet dataviz\\data.xlsx", sheet_name = my_sheet2)
l2015=dfsunburt[2015].tolist()
l2016=dfsunburt[2016].tolist()
l2017=dfsunburt[2017].tolist()
l2015int=[]
l2016int=[]
l2017int=[]
for i in l2015:
    i=int(i)
    l2015int.append(i)
for i in l2016:
    i=int(i)
    l2016int.append(i)
for i in l2017:
    i=int(i)
    l2017int.append(i)






############################################################## Step 3. Create a plotly figure
#########first bar chart
fig = go.Figure()
fig.add_trace(go.Bar(
    x=years,
    y=l1,
    name='première ligne',
    marker_color='RGB(245, 186, 152)'
))
fig.add_trace(go.Bar(
    x=years,
    y=l2,
    name='deuxième ligne',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=years,
    y=l3,
    name='troisième ligne',
    marker_color='rgb(146,197,222)'
))
figbarfirst=fig.update_layout(barmode='group', 
xaxis_tickangle=-30,
width=800,
height=500,
yaxis=dict(titlefont=dict(size=30),))
fighist= go.Figure(data=[go.Bar(
    x=years,
    y=ltot,marker_color='rgb(178,24,43)',text=ltot,
            textposition='auto',width=0.5)])
fighist.update_layout(title_text="Total des passages aux urgences par années",xaxis_type='category')
################pie chart 
figpie = go.Figure(data=[go.Pie(labels=years, values=ltot, hole=.4)])
figpie.update_traces( marker=dict(colors=['rgb(5,48,97)','rgb(178,24,43)','rgb(103,0,31)']))
figpie.update_layout(title_text="Total des passages aux urgences par années")
################ sunburt
#color=[]
"""figsunburt=go.Figure()
def updatefigsunburt(listyear):
    figsunburt =go.Sunburst(
        labels=["Ariana", "Ben Arous", "Mannouba", "Tunis","Grand Tunis", "Bizerte", "Nabeul","Nord-Est", "Kairouan","Centre-Ouest", "Mahdia", "Monastir", "Sfax", "Sousse","Centre-Est", "Medenine", "Sud-Est","Total"],
        parents=["Grand Tunis", "Grand Tunis", "Grand Tunis", "Grand Tunis","Total", "Nord-Est", "Nord-Est","Total", "Centre-Ouest","Total", "Centre-Est", "Centre-Est", "Centre-Est", "Centre-Est","Total","Sud-Est" ,"Total",""],
        values=listyear,  
        branchvalues='total', 
        # marker = {"colors":color},
    )
    #figsunburt=figsunburt.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    return figsunburt

figsunburt2015=updatefigsunburt(l2015int)
figsunburt2016=updatefigsunburt(l2016int)
figsunburt2017=updatefigsunburt(l2017int)"""
figsunburt2015 =go.Figure(go.Sunburst(
    labels=["Ariana", "Ben Arous", "Mannouba", "Tunis","Grand Tunis", "Bizerte", "Nabeul","Nord-Est", "Kairouan","Centre-Ouest", "Mahdia", "Monastir", "Sfax", "Sousse","Centre-Est", "Medenine", "Sud-Est","Total"],
    parents=["Grand Tunis", "Grand Tunis", "Grand Tunis", "Grand Tunis","Total", "Nord-Est", "Nord-Est","Total", "Centre-Ouest","Total", "Centre-Est", "Centre-Est", "Centre-Est", "Centre-Est","Total","Sud-Est" ,"Total",""],
    values=l2015int,
    branchvalues='total'
       
))
figsunburt2015.update_layout(margin = dict(t=0, l=0, r=0, b=0))
figsunburt2016 =go.Figure(go.Sunburst(
        labels=["Ariana", "Ben Arous", "Mannouba", "Tunis","Grand Tunis", "Bizerte", "Nabeul","Nord-Est", "Kairouan","Centre-Ouest", "Mahdia", "Monastir", "Sfax", "Sousse","Centre-Est", "Medenine", "Sud-Est","Total"],
        parents=["Grand Tunis", "Grand Tunis", "Grand Tunis", "Grand Tunis","Total", "Nord-Est", "Nord-Est","Total", "Centre-Ouest","Total", "Centre-Est", "Centre-Est", "Centre-Est", "Centre-Est","Total","Sud-Est" ,"Total",""],
        values=l2016int,
        branchvalues='total'
       
        ))
figsunburt2016.update_layout(margin = dict(t=0, l=0, r=0, b=0))
figsunburt2017 =go.Figure(go.Sunburst(
        labels=["Ariana", "Ben Arous", "Mannouba", "Tunis","Grand Tunis", "Bizerte", "Nabeul","Nord-Est", "Kairouan","Centre-Ouest", "Mahdia", "Monastir", "Sfax", "Sousse","Centre-Est", "Medenine", "Sud-Est","Total"],
        parents=["Grand Tunis", "Grand Tunis", "Grand Tunis", "Grand Tunis","Total", "Nord-Est", "Nord-Est","Total", "Centre-Ouest","Total", "Centre-Est", "Centre-Est", "Centre-Est", "Centre-Est","Total","Sud-Est" ,"Total",""],
        values=l2017int,
       
        ))
figsunburt2017.update_layout(margin = dict(t=0, l=0, r=0, b=0))

figsunburt=go.Figure()
##############  Horizontal bar chart 
opthor=['tous les lignes','première ligne','deuxième ligne','troisième ligne']
dfhorizon = pd.read_excel("C:\\Users\\Ayachi\\Desktop\\projet dataviz\\consultationexterne.xlsx")
lhorizon=dfhorizon.values.tolist()
lh1=lhorizon[1]
lh2=lhorizon[2]
lh3=lhorizon[3]
lhtot=lhorizon[4]
lh1int=[]
lh2int=[]
lh3int=[]
lhtotint=[]
del lh1[0]
del lh2[0]
del lh3[0]
del lhtot[0]
#ligne 1
for i in lh1:
    i=int(i)
    lh1int.append(i)
lh1inttot=lh1int[:3]
lh1intspec=lh1int[3:6]
lh1intgen=lh1int[6:]
# ligne 2
for i in lh2:
    i=int(i)
    lh2int.append(i)
lh2inttot=lh2int[:3]
lh2intspec=lh2int[3:6]
lh2intgen=lh2int[6:]
# ligne 3
for i in lh3:
    i=int(i)
    lh3int.append(i)
lh3inttot=lh3int[:3]
lh3intspec=lh3int[3:6]
lh3intgen=lh3int[6:]
# ligne total
for i in lhtot:
    i=int(i)
    lhtotint.append(i)
lhtotinttot=lhtotint[:3]
lhtotintspec=lhtotint[3:6]
lhtotintgen=lhtotint[6:]



# horizontale ligne 1 
fighoriz1= go.Figure()
fighoriz1.add_trace(go.Bar(
    y=years,
    x=lh1intspec,
    name='Médecine Spécialisée',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(255,99,71)',
        line=dict(color='rgb(255,99,71)', width=2)
    )
))
fighoriz1.add_trace(go.Bar(
    y=years,
    x=lh1intgen,
    name='Médecine Générale ',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(153,50,204)',
        line=dict(color='rgb(153,50,204)', width=2)
    )
))
fighoriz1.update_layout(barmode='stack',title_text="",yaxis_type='category')
## horizontale tous les lignes 
fighoriztot= go.Figure()
fighoriztot.add_trace(go.Bar(
    y=opthor[1:],
    x=[sum(lh1intspec),sum(lh2intspec),sum(lh3intspec)],
    name='Médecine Spécialisée',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(255,99,71)',
        line=dict(color='rgb(255,99,71)', width=2)
    )
))
fighoriztot.add_trace(go.Bar(
    y=opthor[1:],
    x=[sum(lh1intgen),sum(lh2intgen),sum(lh3intgen)],
    name='Médecine Générale ',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(153,50,204)',
        line=dict(color='rgb(153,50,204)', width=2)
    )
))
fighoriztot.update_layout(barmode='stack',title_text="",yaxis_type='category')
# horizontale ligne 2 
fighoriz2= go.Figure()
fighoriz2.add_trace(go.Bar(
    y=years,
    x=lh1intspec,
    name='Médecine Spécialisée',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(255,99,71)',
        line=dict(color='rgb(255,99,71)', width=2)
    )
))
fighoriz2.add_trace(go.Bar(
    y=years,
    x=lh2intgen,
    name='Médecine Générale ',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(153,50,204)',
        line=dict(color='rgb(153,50,204)', width=2)
    )
))
fighoriz2.update_layout(barmode='stack',title_text="",yaxis_type='category')
# horizontale ligne 2 
fighoriz3= go.Figure()
fighoriz3.add_trace(go.Bar(
    y=years,
    x=lh1intspec,
    name='Médecine Spécialisée',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(255,99,71)',
        line=dict(color='rgb(255,99,71)', width=2)
    )
))
fighoriz3.add_trace(go.Bar(
    y=years,
    x=lh3intgen,
    name='Médecine Générale ',
    orientation='h',
    width=0.5,
    marker=dict(
        color='rgb(153,50,204)',
        line=dict(color='rgb(153,50,204)', width=2)
    )
))
fighoriz3.update_layout(barmode='stack',title_text="",yaxis_type='category')
###################### line chart DMS IRL TOM
ind=['DMS','TOM','IRL']
my_sheet4 = 'indicActhospital' 
dfline = pd.read_excel("C:\\Users\\Ayachi\\Desktop\\projet dataviz\\data.xlsx", sheet_name = my_sheet4)
lline=dfline.values.tolist()
#ligne 1
lline1=lline[2]
del lline1[0]
lline1DMS=lline1[:3]
lline1TOM=lline1[3:6]
lline1IRL=lline1[6:]
#ligne 2
lline2=lline[3]
del lline2[0]
lline2DMS=lline2[:3]
lline2TOM=lline2[3:6]
lline2IRL=lline2[6:]
#ligne 3
lline3=lline[4]
del lline3[0]
lline3DMS=lline3[:3]
lline3TOM=lline3[3:6]
lline3IRL=lline3[6:]
###### chart Line 
##DMS
figlineDMS = go.Figure()

figlineDMS.add_trace(go.Scatter(
    x= years,
    y=lline1DMS,
    name = 'première ligne', 
    connectgaps=True # override default to connect the gaps
))
figlineDMS.add_trace(go.Scatter(
    x=years,
    y=lline2DMS,
    name='deuxième ligne',
))
figlineDMS.add_trace(go.Scatter(
    x=years,
    y=lline3DMS,
    name='troisième ligne',
))
figlineDMS.update_layout(title_text="",xaxis_type='category')
####IRL
figlineIRL = go.Figure()

figlineIRL.add_trace(go.Scatter(
    x= years,
    y=lline1IRL,
    name = 'première ligne', 
    connectgaps=True # override default to connect the gaps
))
figlineIRL.add_trace(go.Scatter(
    x=years,
    y=lline2IRL,
    name='deuxième ligne',
))
figlineIRL.add_trace(go.Scatter(
    x=years,
    y=lline3IRL,
    name='troisième ligne',
))
figlineIRL.update_layout(title_text="",xaxis_type='category')
figlineTOM = go.Figure()

figlineTOM.add_trace(go.Scatter(
    x= years,
    y=lline1TOM,
    name = 'première ligne', 
    connectgaps=True # override default to connect the gaps
))
figlineTOM.add_trace(go.Scatter(
    x=years,
    y=lline2TOM,
    name='deuxième ligne',
))
figlineTOM.add_trace(go.Scatter(
    x=years,
    y=lline3TOM,
    name='troisième ligne',
))
figlineTOM.update_layout(title_text="",xaxis_type='category')
########################################################### Step 4. Create a Dash layout
app.layout = html.Div([
     
dbc.Row(
        dbc.Col([
        html.H1('Tableau Activités ambulatoires')
        ]),
),
dbc.Row(
        dbc.Col(html.H5("Passage aux urgences par ligne")
        ),
                
    ),
    
#3333333333rowwwwwwwwwwwwwwwwwwwwwwwww
    ##### dropdown and slider  
dbc.Row(
    [
        dbc.Col([
            "Veuillez choisir une ligne:",
            dcc.Dropdown(
                id="optligne",
                options=[{
                'label': i,
                'value': i } for i in opts],
                value='tous les lignes',
                searchable=False)
        ]),


        dbc.Col([
            "Passage aux urgences en troisième ligne par année:",
            dcc.Slider(
                id='slideansun',
                min=0,
                max=2,
                value=0,
                step=None,
                marks={
                    0: '2015',
                    1: '2016',
                    2: '2017'
                },
                #included=False
            ),   

        ])

    ],align="start",
),
######## les deux graphs : barchart et SUNBURT
dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id = 'plot',figure=figbarfirst,)
        ),

        dbc.Col(

            dcc.Graph(id = 'plotsunburt')
        ),

    ],no_gutters=True,
),
########
dbc.Row(
    [    
        dbc.Col([
            html.H5("Consultations Externes")
            
        ]),
        dbc.Col(
             html.H5("Indicateurs d’activits  hospitalières")

        ),
        
    ],
    
),
dbc.Row(
    [    
        dbc.Col([
            "Veuillez choisir une ligne:",
            dcc.Dropdown(
                id="opthoriz",
                options=[{
                'label': i,
                'value': i } for i in opthor],
                value='tous les lignes',
                searchable=False),
            dcc.Graph(id = 'barhorizon',figure=fighoriztot)
        ]),

        dbc.Col([
            "Veuillez choisir un indicateur:",
            dcc.Dropdown(
                id="optind",
                options=[{
                'label': i,
                'value': i } for i in ind],
                value='DMS',
                searchable=False),
            dcc.RadioItems(
                id="checkline",
                options=[
                {'label': 'tous les lignes', 'value': 'TLL'},
                {'label': 'Première ligne', 'value': 'PL'},
                {'label': 'Deuxième ligne', 'value': 'DL'},
                {'label': 'troisième ligne', 'value': 'TL'}],
            labelStyle={'display': 'inline-block'}
            ),  
            dcc.Graph(id = 'plotline',figure=figlineDMS)
        ]),

        
    ],
    
),
dbc.Row(
    [    
        dbc.Col([
            
        ]),
        dbc.Col(
            html.Div()

        ),
        
    ],
    
),

               

#style = {'padding' : '50px' ,'backgroundColor' : '#EFEFEF'},
])
################################################### Step 5. Add callback functions
##################### Dropdown first bar chart  
@app.callback(Output('plot', 'figure'),
             [Input('optligne', 'value')])
def update_firstbars(ligne):
    if ligne == "tous les lignes":
        fig = figbarfirst
    else:
        if ligne =='première ligne':
            fig = go.Figure(data=[go.Bar(x=years, y=l1,text=l1,
            textposition='auto',width=0.5)])
            fig=fig.update_traces(marker_color='RGB(245, 186, 152)', marker_line_color='rgb(200, 88, 108)',
                  marker_line_width=1.5)
            fig=fig.update_layout(xaxis_type='category',width=760, height=500,title_text="les passages aux urgences en première ligne")

        if ligne == 'deuxième ligne':
            fig = go.Figure(data=[go.Bar(x=years, y=l2,text=l2,
            textposition='auto',width=0.5)])
            fig =fig.update_traces(marker_color='indianred', marker_line_color='RGB(245, 186, 152)',
            marker_line_width=0.5)
            fig=fig.update_layout(xaxis_type='category',width=760, height=500,title_text="les passages aux urgences en deuxième ligne")

        
        if ligne =='troisième ligne':
            fig = go.Figure(data=[go.Bar(x=years, y=l3,text=l3,
            textposition='auto',width=0.5)])
            fig =fig.update_traces(marker_color='rgb(146,197,222)', marker_line_color='rgb(251, 230, 197)',
            marker_line_width=0.5)
            fig=fig.update_layout(xaxis_type='category',width=760, height=500,title_text="les passages aux urgences en troisième ligne")
        if ligne =='Total':
            fig=fighist
    return fig

################## sunburt slider
@app.callback(Output('plotsunburt', 'figure'),
             [Input('slideansun', 'value')])
def update_plotsunburt(slideansun):
    #global figsunburt
    figsunburt=figsunburt2015
    if slideansun == '2015':
        figsunburt=figsunburt2015
       
    else :
        if slideansun == '2016':
        
            figsunburt=figsunburt2016
        
        if slideansun == '2017':
            figsunburt=figsunburt2017
                
    
    return figsunburt
################    horizontal dropdown 
@app.callback(Output('barhorizon', 'figure'),
             [Input('opthoriz', 'value')])
def update_firstbars(lignehoriz):
    if lignehoriz == "tous les lignes":
        fighoriz = fighoriztot
    else:
        if lignehoriz =='première ligne':
            fighoriz =fighoriz1

        if lignehoriz == 'deuxième ligne':
            fighoriz =fighoriz2
        
        if lignehoriz =='troisième ligne':
            fighoriz =fighoriz3
        
    return fighoriz
################  Indicateurs dropdown line chart and Radioitems
@app.callback(Output('plotline', 'figure'),
             [Input('optind', 'value'),Input('checkline', 'value')])
def update_firstbars(optind,checkline):
    if optind == "DMS":
        figline = figlineDMS
        if checkline =='PL':
            figline = go.Figure(data=[go.Bar(x=years, y=lline1DMS,text=lline1DMS,textposition='auto',width=0.5)])
            figline=figline.update_traces(
            marker_line_width=1.5)
            figline=figline.update_layout(xaxis_type='category',title_text="")
        if checkline=='DL':
            figline = go.Figure(data=[go.Bar(x=years, y=lline2DMS,text=lline2DMS,textposition='auto',width=0.5)])
            figline=figline.update_traces(marker_color='rgb(178,34,34)', marker_line_color='rgb(178,34,34)',
            marker_line_width=1.5)
            figline=figline.update_layout(xaxis_type='category',title_text="")
        if checkline=='TL':
            figline = go.Figure(data=[go.Bar(x=years, y=lline3DMS,text=lline3DMS,textposition='auto',width=0.5)])
            figline=figline.update_traces(marker_color='rgb(60,179,113)', marker_line_color='rgb(60,179,113)',
            marker_line_width=1.5)
            figline=figline.update_layout(xaxis_type='category',title_text="")
    else:
        if optind =='IRL':
            figline = figlineIRL
            if checkline =='PL':
                figline = go.Figure(data=[go.Bar(x=years, y=lline1IRL,text=lline1IRL,textposition='auto',width=0.5)])
                figline=figline.update_traces(
                marker_line_width=1.5)
                figline=figline.update_layout(xaxis_type='category',title_text="")
            if checkline=='DL':
                figline = go.Figure(data=[go.Bar(x=years, y=lline2IRL,text=lline2IRL,textposition='auto',width=0.5)])
                figline=figline.update_traces(marker_color='rgb(178,34,34)',
                marker_line_width=1.5)
                figline=figline.update_layout(xaxis_type='category',title_text="")
            if checkline=='TL':
                figline = go.Figure(data=[go.Bar(x=years, y=lline3IRL,text=lline3IRL,textposition='auto',width=0.5)])
                figline=figline.update_traces(marker_color='rgb(60,179,113)',
                marker_line_width=1.5)
                figline=figline.update_layout(xaxis_type='category',title_text="")
            

        if optind == 'TOM':
            figline = figlineTOM
            if checkline =='PL':
                figline = go.Figure(data=[go.Bar(x=years, y=lline1TOM,text=lline1TOM,textposition='auto',width=0.5)])
                figline=figline.update_traces(
                marker_line_width=1.5)
                figline=figline.update_layout(xaxis_type='category',title_text="")
            if checkline=='DL':
                figline = go.Figure(data=[go.Bar(x=years, y=lline2TOM,text=lline2TOM,textposition='auto',width=0.5)])
                figline=figline.update_traces(marker_color='rgb(178,34,34)', 
                marker_line_width=1.5)
                figline=figline.update_layout(xaxis_type='category',title_text="")
            if checkline=='TL':
                figline = go.Figure(data=[go.Bar(x=years, y=lline3TOM,text=lline3TOM,textposition='auto',width=0.5)])
                figline=figline.update_traces(marker_color='rgb(60,179,113)',
                marker_line_width=1.5)
                figline=figline.update_layout(xaxis_type='category',title_text="")
        
    return figline

################# Step 6. Add the server clause
if __name__ == '__main__':
 app.run_server(debug=True)

