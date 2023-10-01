import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Exploration Page",
    page_icon="👀",
    # layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Welcome to My Data Science APP"
    }
)

with st.sidebar:
    st.write("# Data Analysis")
    st.write(":red[***Exploratory Data Analysis(EDA)***] is the process of understanding and summarizing data through statistical and numerical methods, to uncover insights and patterns.")

st.title("Common ML Dataset Explorer")
st.subheader("Datasets For ML Explorer with Streamlit")
header = """ 
<div style="background-color:#e83225;"><p style="color:white;font-size:50px;padding:10px">Streamlit is Awesome</p></div>
"""
st.markdown(header,unsafe_allow_html=True)

st.divider()

def choose_file(path='./datasets'):
        filenames = os.listdir(path)
        selected_filename = st.selectbox("Select A file",filenames)
        return os.path.join(path,selected_filename)
filename = choose_file()
st.info("You Selected {}".format(filename))

st.subheader("Show the Dataset")
df = pd.read_csv(filename)
rows = st.slider("Select no of rows",1,df.shape[0],5)
st.dataframe(df.head(int(rows)))

if st.checkbox("Shape of Dataset"):
    col1, col2, col3 = st.columns(3)
    col1.metric(":blue[Rows]", df.shape[0])
    col2.metric(":green[Columns]",df.shape[1])
    col3.metric(":red[Size]", df.size)

def columns(df):
    return df.columns

cols = columns(df)

with st.expander("Columns of Dataset"):
    st.subheader("Columns and there :blue[Datatypes]")
    st.dataframe(df.dtypes)

with st.expander("Statistics of the Data"):
    st.write("#### Summary Statistics")
    st.dataframe(df.describe())

st.write("##### ***Null Values***")
st.info(f" Are there Any null values: **:green[{bool(df.isna().any().sum())}]**")

if bool(df.isna().any().sum()) == True:
    dropna = st.radio("Drop Null Values",["yes","no"])
        
    if dropna == "yes":
            df.dropna(inplace=True)
            st.success(f"Null Values are droped🎉")	
    else:
            st.warning("The null values might create a problem")

if st.checkbox("Value Counts"):
        try:
            st.text("Value Counts By Target/Class")
            sel = st.multiselect("Choose columns",cols)
            st.dataframe(df.groupby(sel).size()[:10])
        except:
            st.warning("Please select specific Column")

if "data" not in st.session_state:
    st.session_state["data"] = df
else:
    st.session_state['data'] = df

# import numpy as np
# df.loc[len(df)] = [np.nan,np.nan,2.3,1.2,"Iris-setosa"]