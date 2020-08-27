# -3- coding: utf-8 -3-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
################################################################ Step 1. Launch the application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
############################################################### Step 2. Import the dataset 
my_sheet = 'nature handicap'
dfhand= pd.read_excel("C:\\Users\\Ayachi\\Desktop\\projet dataviz\\Maladies+handicaps.xlsx", sheet_name = my_sheet)
#print(dfhand.columns.tolist())
my_sheet2 = 'maladies transmissibles'
dfmal= pd.read_excel("C:\\Users\\Ayachi\\Desktop\\projet dataviz\\Maladies+handicaps.xlsx", sheet_name = my_sheet2)
############################################################## Step 3. Create a plotly figure
######### First Sunburt % handicap
intervale = ["0-14 ans", "15-59 ans", "60 ans et plus", "0-14 ans", "15-59 ans", "60 ans et plus", "0-14 ans", "15-59 ans", "60 ans et plus", "0-14 ans", "15-59 ans", "60 ans et plus"]
sexe = ["Masculin", "Masculin", "Masculin", "Feminin", "Feminin",
           "Feminin","Masculin", "Masculin", "Masculin", "Feminin", "Feminin",
           "Feminin"]
milieu = ["Milieu urbain", "Milieu urbain", "Milieu urbain", "Milieu urbain", "Milieu urbain",
           "Milieu urbain", "Milieu rural ", "Milieu rural ", "Milieu rural ", "Milieu rural ", "Milieu rural ", "Milieu rural "]
valeurs = [2272, 15029,5971,1609,10150,5768,1330,9670,4383,1048,6195,3247]
dfhandage = pd.DataFrame(
    dict(intervale=intervale, sexe=sexe, milieu=milieu, valeurs=valeurs)
)
fighand = px.sunburst(dfhandage, path=['sexe', 'milieu', 'intervale'], values='valeurs')
###### 
color=[ 'rgb(178,24,43)', 'rgb(214,96,77)', 'rgb(244,165,130)', 'rgb(253,219,199)', 
        'rgb(247,247,247)', 'rgb(209,229,240)', 'rgb(146,197,222)', 'rgb(67,147,195)', 'rgb(33,102,172)',
        'rgb(5,48,97)','rgb(146,197,222)']


#liste column nature
nathand=[]
nathand=dfhand['Type handicap'].tolist()
del nathand[0:2]
nathandstr=[]
for i in nathand:
    i=str(i)
    nathandstr.append(i)
#pie chart list
tothand=dfhand["tot"].tolist()
tothandstr=[]
del tothand[0:2]
del tothand[7]
for i in tothand:
    
    i=float(i)
    tothandstr.append(i)
handline=dfhand.values.tolist()
hv0=handline[2]
ho0=handline[3]
mr0=handline[4]
C0=handline[5]
mh0=handline[6]
com0=handline[7]
multi0=handline[8]
#handicap visual list line
hv=[]
ho=[]
mr=[]
C=[]
mh=[]
com=[]
multi=[]
del hv0[0]
for i in hv0:
    i=float(i)
    hv.append(i)
del ho0[0]
for i in ho0:
    i=float(i)
    ho.append(i)
del mr0[0]
for i in mr0:
    i=float(i)
    mr.append(i)
del C0[0]
for i in C0:
    i=float(i)
    C.append(i)
del mh0[0]
for i in mh0:
    i=float(i)
    mh.append(i)
del multi0[0]
for i in multi0:
    i=float(i)
    multi.append(i)
del com0[0]
for i in com0:
    i=float(i)
    com.append(i)


sexeaxe=["Feminin","Masculin"]
milieuaxe=[ "Milieu urbain", "Milieu rural "]
figpie = go.Figure(data=[go.Pie(labels=nathandstr[:7], values=tothandstr, hole=.4)])
#figpie.update_traces( marker=dict(colors=['rgb(5,48,97)','rgb(178,24,43)','rgb(103,0,31)']))
#figpie.update_layout(title_text="")
#handicap visual total
fighv = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[hv[0],hv[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[hv[1],hv[4]],width = 0.35,textposition='auto',)
])
fighv.update_layout(width=600,
    height=500,barmode='stack')
##### 22 
figho = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[ho[0],ho[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[ho[1],ho[4]],width = 0.35,textposition='auto',)
])
figho.update_layout(width=600,height=500,barmode='stack')
##### 3
figmr = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[mr[0],mr[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[mr[1],mr[4]],width = 0.35,textposition='auto',)
])
figmr.update_layout(width=600,height=500,barmode='stack')
####444
figC = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[C[0],C[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[C[1],C[4]],width = 0.35,textposition='auto',)
])
figC.update_layout(width=600,height=500,barmode='stack')
#### 5555 
figcom = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[com[0],com[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[com[1],com[4]],width = 0.35,textposition='auto',)
])
figcom.update_layout(width=600,height=500,barmode='stack')
###6
figmh = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[mh[0],mh[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[mh[1],mh[4]],width = 0.35,textposition='auto',)
])
figmh.update_layout(width=600,height=500,barmode='stack')
#### 777 
figmulti = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[multi[0],multi[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[multi[1],multi[4]],width = 0.35,textposition='auto',)
])
figmulti.update_layout(width=600,height=500,barmode='stack')
# 888
figcom = go.Figure(data=[
    go.Bar(name='masculin', x=milieuaxe, y=[com[0],com[3]],width = 0.35,textposition='auto',),
    go.Bar(name='Feminin', x=milieuaxe, y=[com[1],com[4]],width = 0.35,textposition='auto',)
])
figcom.update_layout(width=600,height=500,barmode='stack')
################################ slider w l cheklist row l theni 
an=['2010','2011','2012','2013','2014','2015','2016','2017']
typemal0=dfmal["Maladies"].tolist()
typemal=[]
for i in typemal0 :
    i=str(i)
    typemal.append(i)
tot=typemal[25]
del typemal[25]
#les listes des columns anneess
#2010
l2010=dfmal["annee 2010"].tolist()
l2010int=[]
for i in l2010:
    i=int(i)
    l2010int.append(i)
#2011
l2011=dfmal["annee 2011"].tolist()
l2011int=[]
for i in l2011:
    i=int(i)
    l2011int.append(i)
#2012
l2012=dfmal["annee 2012"].tolist()
l2012int=[]
for i in l2012:
    i=int(i)
    l2012int.append(i)
#2013
l2013=dfmal["annee 2013"].tolist()
l2013int=[]
for i in l2013:
    i=int(i)
    l2013int.append(i)
#2014
l2014=dfmal["annee 2014"].tolist()
l2014int=[]
for i in l2014:
    i=int(i)
    l2014int.append(i)
#2015
l2015=dfmal["annee 2015"].tolist()
l2015int=[]
for i in l2015:
    i=int(i)
    l2015int.append(i)
#2016
l2016=dfmal["annee 2016"].tolist()
l2016int=[]
for i in l2016:
    i=int(i)
    l2016int.append(i)
#2017
l2017=dfmal["annee 2017"].tolist()
l2017int=[]
for i in l2017:
    i=int(i)
    l2017int.append(i)
# pie total 
figpie2010 = go.Figure(data=[go.Pie(labels=typemal, values=l2010int[:25])])
figpie2011 = go.Figure(data=[go.Pie(labels=typemal, values=l2011int[:25])])
figpie2012 = go.Figure(data=[go.Pie(labels=typemal, values=l2012int[:25])])
figpie2013 = go.Figure(data=[go.Pie(labels=typemal, values=l2013int[:25])])
figpie2014 = go.Figure(data=[go.Pie(labels=typemal, values=l2014int[:25])])
figpie2015 = go.Figure(data=[go.Pie(labels=typemal, values=l2015int[:25])])
figpie2016 = go.Figure(data=[go.Pie(labels=typemal, values=l2016int[:25])])
figpie2017 = go.Figure(data=[go.Pie(labels=typemal, values=l2017int[:25])])
### les liges selon maladies 
dfmaline=dfmal.values.tolist()
# l1 000000000
fv0=dfmaline[0]
fv=[]
del fv0[0]
for i in fv0:
    i=int(i)
    fv.append(i)
fig1 = go.Figure(data=[go.Bar(
            y=fv, 
            x=an,
            text=fv,
            marker_color='rgb(146,197,222)',
            textposition='auto',
            width=0.3)])
# l2 11111
l20=dfmaline[1]
l2=[]
del l20[0]
for i in l20:
    i=int(i)
    l2.append(i)
fig2 = go.Figure(data=[go.Bar(
            y=l2, 
            x=an,
            text=l2,
            textposition='auto',
            width=0.3)])
# l3 22222
l30=dfmaline[2]
l3=[]
del l30[0]
for i in l30:
    i=int(i)
    l3.append(i)
fig3 = go.Figure(data=[go.Bar(
            y=l3, 
            x=an,
            text=l3,
            textposition='auto',
            width=0.3)])
# l4 333333
l40=dfmaline[3]
l4=[]
del l40[0]
for i in l40:
    i=int(i)
    l4.append(i)
fig4= go.Figure(data=[go.Bar(
            y=l4, 
            x=an,
            text=l4,
            textposition='auto',
            width=0.3)])
# l5 4444444444
l50=dfmaline[4]
l5=[]
del l50[0]
for i in l50:
    i=int(i)
    l5.append(i)
fig5 = go.Figure(data=[go.Bar(
            y=l5, 
            x=an,
            text=l5,
            textposition='auto',
            width=0.3)])
# l6 555555
l60=dfmaline[5]
l6=[]
del l60[0]
for i in l60:
    i=int(i)
    l6.append(i)
fig6 = go.Figure(data=[go.Bar(
            y=l6, 
            x=an,
            text=l6,
            textposition='auto',
            width=0.3)])
# l7 6666666666666
l70=dfmaline[6]
l7=[]
del l70[0]
for i in l70:
    i=int(i)
    l7.append(i)
fig7 = go.Figure(data=[go.Bar(
            y=l7, 
            x=an,
            text=l7,
            textposition='auto',
            width=0.3)])
# l8 777777777777
l80=dfmaline[7]
l8=[]
del l80[0]
for i in l80:
    i=int(i)
    l8.append(i)
fig8 = go.Figure(data=[go.Bar(
            y=l8, 
            x=an,
            text=l8,
            textposition='auto',
            width=0.3)])
# l9 
l90=dfmaline[8]
l9=[]
del l90[0]
for i in l90:
    i=int(i)
    l9.append(i)
fig9 = go.Figure(data=[go.Bar(
            y=l9, 
            x=an,
            text=l9,
            textposition='auto',
            width=0.3)])
# l10 
l100=dfmaline[9]
l10=[]
del l100[0]
for i in l100:
    i=int(i)
    l10.append(i)
fig10 = go.Figure(data=[go.Bar(
            y=l10, 
            x=an,
            text=l10,
            textposition='auto',
            width=0.3)])
# l11 
l110=dfmaline[10]
l11=[]
del l110[0]
for i in l110:
    i=int(i)
    l11.append(i)
fig11 = go.Figure(data=[go.Bar(
            y=l11, 
            x=an,
            text=l11,
            textposition='auto',
            width=0.3)])
# l12 
l120=dfmaline[11]
l12=[]
del l120[0]
for i in l120:
    i=int(i)
    l12.append(i)
fig12 = go.Figure(data=[go.Bar(
            y=l12, 
            x=an,
            text=l12,
            textposition='auto',
            width=0.3)])
# l13 
l130=dfmaline[12]
l13=[]
del l130[0]
for i in l130:
    i=int(i)
    l13.append(i)
fig13 = go.Figure(data=[go.Bar(
            y=l13, 
            x=an,
            text=l13,
            textposition='auto',
            width=0.3)])
# l14 
l140=dfmaline[13]
l14=[]
del l140[0]
for i in l140:
    i=int(i)
    l14.append(i)
fig14 = go.Figure(data=[go.Bar(
            y=l14, 
            x=an,
            text=l14,
            textposition='auto',
            width=0.3)])
# l15 
l150=dfmaline[14]
l15=[]
del l150[0]
for i in l150:
    i=int(i)
    l15.append(i)
fig15 = go.Figure(data=[go.Bar(
            y=l15, 
            x=an,
            text=l15,
            textposition='auto',
            width=0.3)])
# l16 
l160=dfmaline[15]
l16=[]
del l160[0]
for i in l160:
    i=int(i)
    l16.append(i)
fig16 = go.Figure(data=[go.Bar(
            y=l16, 
            x=an,
            text=l16,
            textposition='auto',
            width=0.3)])
# l17 
l170=dfmaline[16]
l17=[]
del l170[0]
for i in l170:
    i=int(i)
    l17.append(i)
fig17 = go.Figure(data=[go.Bar(
            y=l17, 
            x=an,
            text=l17,
            textposition='auto',
            width=0.3)])
# l18 
l180=dfmaline[17]
l18=[]
del l180[0]
for i in l180:
    i=int(i)
    l18.append(i)
fig18 = go.Figure(data=[go.Bar(
            y=l18, 
            x=an,
            text=l18,
            textposition='auto',
            width=0.3)])
# l19 
l190=dfmaline[18]
l19=[]
del l190[0]
for i in l190:
    i=int(i)
    l19.append(i)
fig19 = go.Figure(data=[go.Bar(
            y=l19, 
            x=an,
            text=l19,
            textposition='auto',
            width=0.3)])
# l20 
l200=dfmaline[19]
l20=[]
del l200[0]
for i in l200:
    i=int(i)
    l20.append(i)
fig20 = go.Figure(data=[go.Bar(
            y=l20, 
            x=an,
            text=l20,
            textposition='auto',
            width=0.3)])
# l21 
l210=dfmaline[20]
l21=[]
del l210[0]
for i in l210:
    i=int(i)
    l21.append(i)
fig21 = go.Figure(data=[go.Bar(
            y=l21, 
            x=an,
            text=l21,
            textposition='auto',
            width=0.3)])
# l22 
l220=dfmaline[21]
l22=[]
del l220[0]
for i in l220:
    i=int(i)
    l22.append(i)
fig22 = go.Figure(data=[go.Bar(
            y=l22, 
            x=an,
            text=l22,
            textposition='auto',
            width=0.3)])
# l23 
l230=dfmaline[22]
l23=[]
del l230[0]
for i in l230:
    i=int(i)
    l23.append(i)
fig23 = go.Figure(data=[go.Bar(
            y=l23, 
            x=an,
            text=l23,
            textposition='auto',
            width=0.3)])
# l24 
l240=dfmaline[23]
l24=[]
del l240[0]
for i in l240:
    i=int(i)
    l24.append(i)
fig24 = go.Figure(data=[go.Bar(
            y=l24, 
            x=an,
            text=l24,
            textposition='auto',
            width=0.3)])
# l25 
l250=dfmaline[24]
l25=[]
del l250[0]
for i in l250:
    i=int(i)
    l25.append(i)
fig25 = go.Figure(data=[go.Bar(
            y=l25, 
            x=an,
            text=l25,
            textposition='auto',
            width=0.3)])



########################################################### Step 4. Create a Dash layout
app.layout = html.Div([ 
dbc.Row(
        dbc.Col([
        html.H1('Tableau :Handicap et Maladies ')
        ]),
),
dbc.Row(
        
        
                
),
dbc.Row([
        
        dbc.Col([
            html.H3("Handicap"),
            "1. Répartition des hadicapés porteurs des cartes d’hadicap selon le milieu et tranche d’âge",
            dcc.Graph(id = 'plot',figure=fighand),
        ]),
        dbc.Col([
            "2. Proportion des hadicapés porteurs des cartes d’hadicap selo le milieu et la nature d’hadicap", 
            dcc.Dropdown(
                id="optnathand",

                options=[{
                'label': i,
                'value': i } for i in nathandstr[:7]],
                value='Handicap visual',
                searchable=False), 
            dcc.Graph(id = 'barhand',figure=fighv),
        ]),
],no_gutters=True,),
###########""
dbc.Row(
        dbc.Col([
        html.H3('les Maladies transmissibles ')
        ]),
),
dbc.Row([
        dbc.Col([
            "veuillez choisir la maladie:",
            dcc.Dropdown(
                id="dropmal",
                options=[{
                'label': i,
                'value': i } for i in typemal],
                value='Fievre typhoide',
                searchable=True
            ),
            dcc.Graph(id = 'bartypemal',figure=fig1)   
        ]),
        dbc.Col([
            dcc.Slider(
                id='slideyear',
                min=0,
                max=7,
                step=None,
                updatemode='drag',
                marks={
                    0: '2010',
                    1: '2011',
                    2: '2012',
                    3: '2013',
                    4: '2014',
                    5: '2015',
                    6: '2016',
                    7: '2017'
                },
                value=0,
                #included=False
            ),
            dcc.Graph(id = 'figpie2',figure=figpie2010),
                
        ]),
]),
###############""
dbc.Row([
        dbc.Col([
            

        ]),
                
]),

####
])   
################################################## Step 5. Add callback functions
##################### Dropdown first bar chart  
@app.callback(Output('bartypemal', 'figure'),
             [Input('dropmal', 'value')])
def update_firstbars(mal):
    global fig
    if mal == "Fievre typhoide":
        fig= fig1
    else:
        if mal =='Elepatites virales':
            fig=fig2
        if mal =='Meningites':
            fig=fig3
        if mal =='Rougeole':
            fig=fig4
        if mal =='Tuberculose':
            fig=fig5
        if mal =='Leishmaniose Cuta':
            fig=fig6
        if mal =='R.A.A':
            fig=fig7
        if mal =='Echinococcose':
            fig=fig8
        if mal =='Syphilis':
            fig=fig9
        if mal =='T.I.A.0':
            fig=fig10
        if mal =='IUG':
            fig=fig11
        if mal == 'Paralysie':
            fig=fig12
        if mal =='Diphterie':
            fig=fig13
        if mal =='Rage':
            fig=fig14
        if mal =='Tetanos neonatal':
            fig=fig15
        if mal =='Tetanos non':
            fig=fig16
        if mal =='Paludisme':
            fig=fig17
        if mal =='Bilharziose':
            fig=fig18
        if mal =='Leishmaniose Visc':
            fig=fig19
        if mal =='Brucellose':
            fig=fig20
        if mal =='Lepre':
            fig=fig21
        if mal =='Leptospirose':
            fig=fig22
        if mal =='SIDA':
            fig=fig23
        if mal =='Rickettsioses':
            fig=fig24
        if mal =='Coqueluche':
            fig=fig25    
    fig=fig.update_layout(xaxis_type='category',title_text="")
    return fig
@app.callback(Output('figpie2', 'figure'),
             [Input('slideyear', 'value')])
def update_pie(slidyear):
    global figslide
    if slidyear == 0:
        figslide= figpie2010
    else:
        if slidyear == 1 :
            figslide=figpie2011
        if slidyear == 2:
            figslide=figpie2012
        if slidyear == 3:
            figslide=figpie2013
        if slidyear == 4  :
            figslide=figpie2014
        if slidyear == 5:
            figslide=figpie2015
        if slidyear == 6:
            figslide=figpie2016
        if slidyear == 7:
            figslide=figpie2017
    figslide.update_traces(textposition='inside')
    figslide.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    
    return figslide
################################
@app.callback(Output('barhand', 'figure'),
             [Input('optnathand', 'value')])
def update_bar(optnat):
    global figbar
    if optnat == "Handicap visual":
        figbar= fighv
    else:
        if optnat == "Handicap oculaire" :
            figbar= figho
        if optnat == "Mobilite recluite" :
            figbar= figmr
        if optnat == "Concentration" :
            figbar= figC
        if optnat == "Membre handicap" :
            figbar= figmh
        if optnat == "Communication" :
            figbar= figcom
        if optnat == "Multi handicap" :
            figbar= figmulti
        
    return figbar

################# Step 6. Add the server clause
if __name__ == '__main__':
 app.run_server(debug=True)
