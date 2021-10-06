import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
import seaborn as sns
import numpy as np


st.title('Radar Chart')

st.sidebar.header('Selections')


df=pd.read_csv('defensive_detail_epl.csv')
df.rename(columns=df.iloc[0], inplace = True)
df.drop([0], inplace = True)


df=df.drop(['Rk','Nation', 'Age', 'Born','Matches'],axis=1)
df['Player']=df['Player'].str.split('\\',expand=True)[0]

df['90s']=pd.to_numeric(df['90s'],downcast='float')
df=df[df['90s']>10].reset_index()

attribute_list = df.columns;
attribute_list=attribute_list[4:]


attribute_list_selection = st.sidebar.multiselect('Please select atleast Three Attribute', attribute_list,)

postion_selected=st.sidebar.selectbox("Postion ", ['ALL','MF','FW','DF'])

if postion_selected != 'ALL':
	df=df[df['Pos'].str.contains(postion_selected)].reset_index(drop=True)

player1_selected = st.sidebar.selectbox("Player 1",df['Player'],1)

player2_selected = st.sidebar.selectbox("Player 2",df['Player'],2)

st.header("Comparing "+player1_selected+" vs "+ player2_selected)
value=st.slider('Ratio', min_value=0, max_value=100)

df1=df[(df['Player']==player1_selected)|(df['Player']==player2_selected)].reset_index(drop=True)

for x in attribute_list_selection:
    df1[x]=pd.to_numeric(df1[x],downcast='float')


ranges=[]
a_values =[]
b_values =[]

player1=df1[df['Player']==player1_selected]
player2=df1[df['Player']==player2_selected]

for x in attribute_list_selection:
    a=min(df1[x])
    a=a*.75
    a_values.append(df1[x][0])
    b_values.append(df1[x][1])
 #   a_values.append(player1[x])
 #   b_values.append(player2[x])    
    b=max(df1[x])
    b=b*1.25
    
    ranges.append((a,b))

values= [a_values,b_values]

endnote ='Data from FBREF'

title = dict(
    title_name = df1.Player[0],
    title_color ='red',
    subtitle_name= df1.Squad[0],
    subtitle_color= 'red',
    title_name_2 = df1.Player[1],
    title_color_2 ='blue',
    subtitle_name_2 = df1.Squad[1],
    subtitle_color_2 = 'blue',
    title_fontsize= 15,
    sbutitle_fontsize=15
)

if len(attribute_list_selection) >2 :
	radar= Radar()

	fig, ax = radar.plot_radar(ranges= ranges, params=attribute_list_selection,values=values,
                           radar_color=['red','blue'],alpha=[.40,.35],title=title,
                           endnote=endnote,compare=True)
	st.pyplot(fig)

