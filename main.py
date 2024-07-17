import streamlit as st
import pandas as pd
import helper as hp
df=pd.read_csv('diabetes.csv')
checker=st.sidebar.button("check")
a=hp.sidebar()
if checker:
    
    d=hp.mainfunc(df,a)

    if d==0:
        st.title("congratulation you are safe")
    else:
        st.title("go to a doctor ")