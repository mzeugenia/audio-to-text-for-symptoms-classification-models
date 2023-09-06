import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import nltk
from nltk.tag import pos_tag
import string
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce
from joblib import load


# Load animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

# Get text input from user
def get_data():
    return []

# Clean input text
def text_process(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    return " ".join(text)

# Stemming words
def stemmer(sentence):
    ps = PorterStemmer()
    words = word_tokenize(sentence)
    # using reduce to apply stemmer to each word and join them back into a string
    stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), words, "")
    return stemmed_sentence


# ---- PAGE ----
st.set_page_config(page_title="SympToMatch", layout="wide")

# ---- HEADER ----
with st.container():
    st.title("SympToMatch")

# ---- LOAD ASSETS  ---- 
lottie_coding = load_lottie_url("https://assets1.lottiefiles.com/temp/lf20_R7WisW.json")

with st.container():
    left_column, right_column = st.columns(2)

    with right_column:
        st_lottie(lottie_coding, height=500, key="nurse_phone")
    
    with left_column:
        st.subheader("Unleashing the power of AI to match patients with the right care.")
        
        # ---- TEXT WIDGET: input ----            
        with st.form(key="text_input_user"):
            text_input = st.text_input("Text input")
            submit_button = st.form_submit_button(label="Submit")
        
            if submit_button and text_input:
                #st.success("Success!")
        
            # ---- TEXT WIDGET: output ----      
            # with st.form(key="text_output_user"):
            # Clean text (text_process)
                text_clean = text_process(text_input)
                
                    # Stremming text (stremmer)
                text_stemmed = stemmer(text_clean)
                st.text_area(label="Output Data:", value=text_stemmed, height=50)
                    # Apply Model_1
                # model_1 = load("severity_classifier_model_1.joblib")
                # output_1 = model_1.predict(text_stemmed)

                    # Apply Model_2