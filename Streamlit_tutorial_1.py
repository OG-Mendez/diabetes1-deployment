import streamlit as st
import pandas as pd
import joblib
from io import BytesIO
import requests # or https

# URL to model in my git repository 
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
        d = "Possible chance of Diabetes - Patient is at risk of having diabetes, for further assistance contact " \
            "FMC-Abuja at +234 7025700037"
    else:
        d = "Patient has a high chance of being diabetic, for further assistance contact FMC-Abuja at +234 7025700037"
    return d


def main():
    # giving the webpage a title
    st.title("Diabetes Prediction")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """ 
    <style>
    .header {
        background: linear-gradient(90deg, rgba(30,144,255,1) 0%, rgba(0,123,255,1) 100%);
        padding: 15px;  /* Reduced padding */
        border-radius: 8px;  /* Slightly smaller border-radius */
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    .header h1 {
        color: white;
        font-family: 'Poppins', sans-serif;
        font-weight: 200;
        font-size: 36px;  /* Slightly smaller font size */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        letter-spacing: 1.5px;  /* Slightly reduced letter spacing */
        margin: 0;
    }
    </style>

    <div class="header"> 
        <h1>Streamlit Diabetes Prediction ML App</h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    Gender = st.selectbox("Gender", ("Male", "Female"), help="Select Gender")
    AGE = st.text_input("Age", placeholder= "Type Here", help="Enter Age")
    #The below code is for error handling
    if AGE:
        try:
            number = float(AGE)  # Try converting input to a float
            AGE = number
        except ValueError:
            st.error('Please enter a valid number.')
    else:
        st.write('Please enter a number.')
    HbA1c = st.text_input("HbA1c (Glycated Haemoglobin)", placeholder= "Type Here", help="Shows what your average "
                                                                                         "blood sugar (glucose) level "
                                                                                         "was over the past two to "
                                                                                         "three months.")
    if HbA1c:
        try:
            number = float(HbA1c)  # Try converting input to a float
            HbA1c = number
        except ValueError:
            st.error('Please enter a valid number.')
    else:
        st.write('Please enter a number.')
    Chol = st.text_input("Cholestrol", placeholder="Type Here", help="If you have too much cholesterol in your blood, "
                                                                     "it can combine with other substances in the blood"
                                                                     " to form plaque. Plaque sticks to the walls of "
                                                                     "your arteries.")
    if Chol:
        try:
            number = float(Chol)  # Try converting input to a float
            Chol = number
        except ValueError:
            st.error('Please enter a valid number.')
    else:
        st.write('Please enter a number.')
    TG = st.text_input("TG (TriGlycerides)", placeholder="Type Here", help="Triglycerides come from the food you "
                                                                           "eat. Extra calories are turned into "
                                                                           "triglycerides and stored in fat cells "
                                                                           "for later use.")
    if TG:
        try:
            number = float(TG)  # Try converting input to a float
            TG = number
        except ValueError:
            st.error('Please enter a valid number.')
    else:
        st.write('Please enter a number.')
    VLDL = st.text_input("VLDL (Very Low Density Lipoprotein)", placeholder="Type Here", help="VLDL is a type of bad "
                                                                                              "cholesterol because it "
                                                                                              "helps cholesterol build "
                                                                                              "up on the walls of "
                                                                                              "arteries.")
    if VLDL:
        try:
            number = float(VLDL)  # Try converting input to a float
            VLDL = number
        except ValueError:
            st.error('Please enter a valid number.')
    else:
        st.write('Please enter a number.')
    BMI = st.text_input("BMI (Body Mass Index)", placeholder="Type Here", help="Body mass index (BMI) is a medical "
                                                                               "screening tool that measures the ratio "
                                                                               "of your height to your weight to estimate "
                                                                               "the amount of body fat you have.")
    if BMI:
        try:
            number = float(BMI)  # Try converting input to a float
            BMI = number
        except ValueError:
            st.error('Please enter a valid number.')
    else:
        st.write('Please enter a number.')



    result = ""
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = pred(Gender, AGE, HbA1c, Chol, TG, VLDL, BMI)
    st.success(result)


if __name__ == '__main__':
    main()
