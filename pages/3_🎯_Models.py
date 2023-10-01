from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression, LogisticRegression
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Model Page",
    page_icon="🧐",
    # layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
	st.write("# Modeling")
	st.write("In data science, :red[***Modeling***] refers to the construction of mathematical or computational frameworks used to analyze and make predictions based on data patterns.")

st.write("# :red[*Dataset*]")
data = st.session_state.data
st.write(data.head(10))

cols = data.columns

st.write("## :violet[Supervised Learning]")
with st.expander("Linear Regression"):
    st.write("## :orange[Linear Regression]")

    op1 = st.selectbox("Choose the **X** values", cols)
    op2 = st.selectbox("Choose the ***y*** values", cols)

    X = data[[op1]].values.astype(int)
    y = data[op2].values.astype(int)

    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)

    ans = st.text_input("Predict a value")
    try:
        st.write("#### The Predicted value is: ", model.predict([[float(ans)]])[0])
    except:
        st.info("Please enter integer values")
    st.divider()

    st.write("##### (**Coefficient**) The amount y changes for a unit increase in x:", model.coef_[0])
    st.write("##### (**Intercept**) The Constant term Y is: ", model.intercept_)
    fig, ax = plt.subplots()

    st.divider()
    ax.scatter(X, y)
    ax.plot(X, y_pred, c='orange')
    ax.set_title("BEST FIT LINE")
    st.pyplot(fig)

with st.expander("Logistic Regression"):
    try:

        st.write("## :orange[Logistic Regression]")

        op3 = st.multiselect("Choose the **X** values", cols)
        op4 = st.multiselect("Choose the ***y*** values", cols)

        try:
            x = data[op3].values
        except:
            st.info("Please select columns with *Integer/Float* values only")
        
        try:
            y = data[op4].values
        except:
            st.info("Please select column with **2-unique** values or *Integers*")

        x_train,x_test,y_train,y_test = train_test_split(x,y,random_state =0)

        model = LogisticRegression()
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)

        st.write(f"#### The accuracy of the model is :green[{round(accuracy_score(y_pred,y_test)*100, 2)}]%")

        ans = st.text_input("Enter the value")
        ans = ans.split(' ') 
        li = []
        for i in ans:
            li.append(float(i))
        st.write("#### The Predicted value is: ", model.predict([li]))
    except:
            # st.info("Write the (**Integer**)values with white space between column values.")
            st.info("Select multiple columns as **Input (X)** and single column for **Output (Y)**.")
