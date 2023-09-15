import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd

# text prpcessing
from cleantext import clean
import nltk
from nltk.tag import pos_tag
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce

from functools import reduce
from joblib import load

# running models
from sklearn.pipeline import make_pipeline
import pickle



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



# Steps to clean input sentence
def do_clean(text):
    """The string (text) is converted to lowercase, it is stripped, and the punctualization is removed."""
    return clean(text, lowercase=True, extra_spaces=False, punct=True)

def text_process(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    return " ".join(text)

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
    st.title(":blue[SympToMatch]")

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
            text_input = st.text_input("Input text", placeholder = "For example: I fell down the stairs and twisted my ankle.")
        
            submit_button = st.form_submit_button(label="Submit", type="primary")

            # Add button with example text
            #if st.button('Use exemple'):
            #    text_input = "I fell down the stairs and twisted my ankle."
        
            if submit_button and text_input:
                #st.success("Success!")
        
            # ---- TEXT WIDGET: output ----      
            # with st.form(key="text_output_user"):
            # Preprocess text
                text_clean = do_clean(text_input)
                text_processed  = text_process(text_clean)
                text_stemmed = stemmer(text_processed)
                

                            
                # Apply Model_1
                # load model 1
                with open('model_1', 'rb') as tm:
                    loaded_model_1 = pickle.load(tm)

                output_model_1 = loaded_model_1.predict(pd.array([text_stemmed]))
                
                if output_model_1 == [1]:
                    severity_level = "severe"
                else:
                    severity_level = "mild"


                # Apply Model_2
                # load model 2
                with open('model_2', 'rb') as tm:
                    loaded_model_2 = pickle.load(tm)

                output_model_2 = loaded_model_2.predict(pd.array([text_stemmed]))
                
                st.text_area(label="Output:", value=(f"Your condition is {severity_level}. We recommend that you book a visit with a specialist in {output_model_2[0]}."))


                