import streamlit as st


with st.container():
    title = '<h1 style="font-family:Verdana, sans-serif; color:#036396; font-weight: 900; font-size: 62px;">SympToMatch</h1>'
    st.markdown(title, unsafe_allow_html=True)
    st.text("") 

with st.container():
    left_column, right_column = st.columns(2)

    with right_column:
        subheader = '<h3 style="font-family: Trebuchet MS, sans-serif; color:#419e8d; font-style: oblique; font-size: 32px;">Unleashing the power of AI to match patients with the right care.</h3>'

    
    with left_column:
        subheader = '<h3 style="font-family: Trebuchet MS, sans-serif; color:#419e8d; font-style: oblique; font-size: 32px;">Unleashing the power of AI to match patients with the right care.</h3>'
        
        st.markdown(subheader, unsafe_allow_html=True)
        st.text("")
        st.text("")


# Create a container for the sentence input
input_container = st.container()
with input_container:
    st.write("Enter a sentence:")
    user_input = st.text_input("Input", st.session_state.get("user_input", ""))

# Create a layout with four columns for the example buttons
col1, col2, col3, col4 = st.columns(4)

# Define example sentences
example_sentences = {
    "Example 1": "I have been feeling extremely anxious and panicky.",
    "Example 2": "I accidentally ingested a toxic substance.",
    "Example 3": "I have been experiencing severe headaches and dizziness.",
    "Example 4": "I have a deep cut on my hand that won't stop bleeding.",
}

# Create buttons for each example sentence in separate columns
if col1.button("Example 1"):
    user_input = example_sentences["Example 1"]
if col2.button("Example 2"):
    user_input = example_sentences["Example 2"]
if col3.button("Example 3"):
    user_input = example_sentences["Example 3"]
if col4.button("Example 4"):
    user_input = example_sentences["Example 4"]

# Store the user_input in session_state
st.session_state.user_input = user_input

# Create a submit button
if input_container.button("Submit", type="primary"):
    
    print("hello")
    # Convert the user_input to uppercase
   # user_input = st.session_state.user_input.upper()
    
# Display the uppercase sentence in a new text_input field
#st.text_input("Uppercase Input", user_input)
    



