from cmath import sqrt
from unittest import result
import streamlit as st
import pandas as pd
import pickle
import numpy as np

pickele_in = open('bhpm.pkl','rb')
lr = pickle.load(pickele_in)

def welcome():
    return 'Welcome !'

def predict_price(location,sqft,bath,bhk):    

    X = np.zeros(244)
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
   

    return np.round(lr.predict([X])[0],2)    

def main():
    home = pd.read_csv('Bengaluru_House_Data.csv')
    loc = home['location'].unique()
    st.title('New App')
    html_temp = """
    <h2 style = "colour:black; text-align:left: ">Streamlit App </h2>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    location = st.selectbox('Locaton',loc)
    st.subheader('Area :')
    sqrt = st.slider('In sq-ft',min_value = 300, max_value = 3000)
    st.subheader('Bathrooms :')
    bath = st.slider('No Of Bathroom',min_value = 1, max_value = 10, step = 1)
    st.subheader('BHK :')
    bhk = st.slider('No Of BHK',min_value = 1, max_value = 10, step = 1)

    result = ""

    if st.button("Result"):
        result = predict_price(location,sqrt,bath,bhk)
        st.success(f'The Final Price Is\f\f{ result}\f/- Lacks')

if __name__ == '__main__':
    main()