import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Chart Page",
    page_icon="📉",
    # layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
	st.write("# Data Visualization")
	st.write(":red[***Data Visualization***] is the graphical representation of data to facilitate the understanding of patterns, trends, and insights within datasets.")

st.write("# :orange[*Dataset*]")
data = st.session_state.data
st.write(data.head())

cols = data.columns
sel1 = st.multiselect("Select the column you want to show: ", cols)

st.divider()
st.write("### :violet[*Line Chart*]")
st.line_chart(data[sel1][:20])

st.divider()
st.write("### :red[*Area Chart*]")
st.area_chart(data[sel1][:20])

st.divider()
st.write("### :green[*Bar Chart*]")
st.bar_chart(data[sel1][:20])

st.divider()
st.write("### :blue[*Count Plot*]")
sel2 = st.selectbox("Select the column you want to show: ", cols)

fig = plt.figure(figsize=(10,4))
sns.countplot(x =str(sel2),data = data[:30])
st.pyplot(fig)