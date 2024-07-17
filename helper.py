import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
def sidebar():
    st.sidebar.title("diabetics prediction")
    pregnency=st.sidebar.slider("select pregnencies",min_value=0,max_value=20,value=2)
    glucose=st.sidebar.slider("Glucose",min_value=0,max_value=200)
    BloodPressure=st.sidebar.slider("BloodPressure",min_value=0,max_value=200)
    SkinThickness=st.sidebar.slider("SkinThickness",min_value=0,max_value=200)
    Insulin=st.sidebar.slider("Insulin",min_value=0,max_value=200)
    BMI=st.sidebar.slider("BMI",min_value=0,max_value=200)
    DiabetesPedigreeFunction=st.sidebar.slider("DiabetesPedigreeFunction",min_value=0,max_value=200)
    Age=st.sidebar.slider("Age",min_value=0,max_value=200)
    values=[pregnency,glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    return pd.DataFrame([values])

def mainfunc(df,a):
   
    sc_fit=StandardScaler()
    b=df.drop(['Outcome'],axis=1)
    x=df.drop(['Outcome'],axis=1)
    x=pd.DataFrame(sc_fit.fit_transform(x),columns=b.columns)
    y=df['Outcome']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    knn=KNeighborsClassifier(13)
    knn.fit(x_train,y_train)
    return knn.predict(a)




