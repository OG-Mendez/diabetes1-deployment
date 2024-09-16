import streamlit as st
import pandas as pd
import joblib
from io import BytesIO
import requests # or https

# e.g. a file call stopwords saved by joblib
# https://github.com/Proteusiq/hisia/v1.0.1/hisia/models/data/stops.pkl

# change github.com to raw.githubusercontent.com

URI = "https://github.com/OG-Mendez/diabetes1-deployment/blob/main/diabetes_model_1.pkl?raw=true"

class InvalidInputError(Exception):
    pass


def welcome():
    return 'welcome all'


def pred(Gender, AGE, HbA1c, Chol, TG, VLDL, BMI):
    if Gender.lower() == "male":
        Gender = 1
    else:
        Gender = 0

    a = {'Gender': Gender, 'AGE': AGE, 'HbA1c': HbA1c, 'Chol': Chol, 'TG': TG, 'VLDL': VLDL, 'BMI': BMI}
    b = pd.DataFrame.from_dict([a])
    print(b)

    clf = joblib.load(BytesIO(requests.get(URI).content))
    c = clf.predict(b)
    if c == 0:
        d = "Little to no chance of patient being diabetic"
    elif c == 1:
        d = "Possible chance of Diabetes - Patient is at risk of having diabetes"
    else:
        d = "Patient has a high chance of being diabetic"
    return d


def main():
    # giving the webpage a title
    st.title("Diabetes Prediction")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Diabetes Prediction ML App </h1> 
    </div> 
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    Gender = st.selectbox("Gender", ("Male", "Female"))
    AGE = st.text_input("Age", placeholder="Type Here")
    HbA1c = st.text_input("HbA1c", placeholder="Type Here")
    Chol = st.text_input("Cholestrol", placeholder="Type Here")
    TG = st.text_input("TG", placeholder="Type Here")
    VLDL = st.text_input("VLDL", placeholder="Type Here")
    BMI = st.text_input("BMI", placeholder="Type Here")

    result = ""
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = pred(Gender, AGE, HbA1c, Chol, TG, VLDL, BMI)
    st.success(result)


if __name__ == '__main__':
    main()
