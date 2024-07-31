import streamlit as st
import pandas as pd
from pathlib import Path
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components


st.title("Hello")
st.text("Please upload your file")
file = st.file_uploader(label= "Your data file", type=['csv','xlsx'],)
if file is not None:
    if Path(file.name).suffix == ".csv":
        df = pd.read_csv(file)
    elif Path(file.name).suffix == ".xlsx":
        df = pd.read_excel(file)
    
    #st.write(df.head())

    # st.write("The non-categorical fields with standard statistics:")
    # st.write(control.describe(df))
    # st.write(control.info(df))
    # st.write(df.info())

    # dv = st.selectbox("Declare your target variable",options=df.columns)

    # x = df.drop(dv,axis=1)
    # y = df[dv]

    profile = ProfileReport(df, title = "EDA Report").to_html()

    st.download_button(
    "Press to Download EDA",
    profile,
    "file.html"
    )
    components.html(profile,height=500*len(df.columns), scrolling= True)

    

        
    