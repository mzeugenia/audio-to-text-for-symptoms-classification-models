import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# text prepcessing
from cleantext import clean
import nltk
from nltk.tag import pos_tag
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce

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


# Steps to preprocess input sentence
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

title = '<h1 style="font-family:Verdana, sans-serif; color:#036396; font-weight: 900; font-size: 62px;">SympToMatch</h1>'
st.markdown(title, unsafe_allow_html=True)
st.text("") 

# ---- LOAD ASSETS  ---- 
lottie_coding = load_lottie_url("https://assets1.lottiefiles.com/temp/lf20_R7WisW.json")

with st.container():
    left_column, right_column = st.columns(2)

    with right_column:
        st_lottie(lottie_coding, height=500, key="nurse_phone")
    
    with left_column:
        subheader = '<h3 style="font-family: Trebuchet MS, sans-serif; color:#419e8d; font-style: normal; font-size: 32px;">Unleashing the power of AI to match patients with the right care.</h3>'
        st.markdown(subheader, unsafe_allow_html=True)
        st.text("")
        st.text("")
       
       
        # ---- TEXT WIDGET: input ----    
        
        # Create a container for the sentence input
        input_container = st.container()
        
        
        with input_container:
            instruction = '<h5 style="font-family: Trebuchet MS, sans-serif; color:black; font-style: normal; font-size: 15px;">Enter a sentence:</h5>'
            st.markdown(instruction, unsafe_allow_html=True)
            st.markdown("For example: *I fell down the stairs and twisted my ankle.*")
            

            # Create a layout with four columns for the example buttons
            example_sentences = [
                "I have been feeling extremely anxious and panicky.",
                "I accidentally ingested a toxic substance.",
                "I have been experiencing severe headaches and dizziness.",
                "I have a deep cut on my hand that won't stop bleeding.",
                "I cut my finger while cooking, and the bleeding doesn't seem to be stopping."
            ]
            cols = st.columns(len(example_sentences))
            example_selected = False

            for index, (col, sentence) in enumerate(zip(cols, example_sentences), 1):
                if col.button(f"Example {index}"):
                    st.session_state.user_input = sentence
                    example_selected = True
            
        
            form = st.form(key='my_form')
            user_input = form.text_input('', '', key='user_input')
            submit_button = form.form_submit_button(label='Submit', type ="primary")                           

        
        
        # In case the `user_input` is provided or selected and the `submit_button` is clicked
        if user_input and (submit_button or example_selected):
            
            # ---- TEXT WIDGET: output ----      
            
            
            # Preprocess text
            text_clean = do_clean(user_input)
            text_processed  = text_process(text_clean)
            text_stemmed = stemmer(text_processed)
                
                            
            # ---- APPLY MODEL 1 ----

            # Load model 1
            with open('model_1', 'rb') as tm:
                loaded_model_1 = pickle.load(tm)
            # Fit model_1
            output_model_1 = loaded_model_1.predict(pd.array([text_stemmed]))
            
            # Convert 0-1 to mild-severe
            if output_model_1 == [1]:
                severity_level = "severe"
            else:
                severity_level = "mild"


            # ---- APPLY MODEL 2 ----
            # Load model 2
            with open('model_2', 'rb') as tm:
                loaded_model_2 = pickle.load(tm)
            # Fit model_2
            output_model_2 = loaded_model_2.predict(pd.array([text_stemmed]))
            
            # Write a comprehensive output sentence
            output_sentence = f"Your condition is {severity_level}. We recommend that you book a visit with a specialist in {output_model_2[0]}."
            st.text("")
            st.text("")
            # Style output format
            final_sentence = '<h5 style="font-family: Trebuchet MS, sans-serif; color:black; font-style: normal; font-size: 15px;">Output:</h5>'
            st.markdown(final_sentence, unsafe_allow_html=True)
            # Print comprehensive output sentence
            st.text_area(label="", value= output_sentence)


            if len(output_sentence)>0:

                # Add plots:        
                with st.container():
                    # Count n words in input sensence.
                    n_words = len(str(user_input).split())
                    st.markdown(f"The sentence has **{n_words}** words.")

                    font1 = {'family':'Helvetica','color':'black','size':20, 'weight' :"bold"}
                    font2 = {'family':'Helvetica','color':'black','size':14, 'weight' :"bold"}
                    
                    test_train_data = pd.read_csv("./data/test_train_data.csv")
                    data = test_train_data.word_count
                    hist_n_words = sns.histplot(data, bins=range(0, 31), color = "#036396")
                    hist_n_words.axvline(x = n_words, color = "red")

                    plt.title("WORDS COUNT IN THE SENTENCE", fontdict=font1)
                    plt.xlabel("WORD COUNT", fontdict=font2)
                    plt.ylabel("COUNT", fontdict=font2)
                    plt.tight_layout()
                    sns.despine()
                    st.pyplot(hist_n_words.get_figure())

                        
                        
                    

                        


                