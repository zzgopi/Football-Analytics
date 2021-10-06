import streamlit as st
import pandas as pd

df=pd.read_csv('defensive_detail_epl.csv')

df.rename(columns=df.iloc[0], inplace = True)
df.drop([0], inplace = True)


df=df.drop(['Rk','Nation', 'Age', 'Born','Matches'],axis=1)

df['Player']=df['Player'].str.split('\\',expand=True)[0]

df['90s']=pd.to_numeric(df['90s'],downcast='float')
df=df[df['90s']>10].reset_index()

list = df.columns;
list=list[4:]

option = st.sidebar.selectbox(
    'Which number do you like best?',
     list)

for x in list:
    df[x]=pd.to_numeric(df[x],downcast='float')
#    df[x]=df[x]/df['90s']

df1=df[(df['Player']=='Rodri')|(df['Player']=='Fred')].reset_index()


'You selected: ', option


hour_to_filter = st.slider('Range', 0, 100, 25)