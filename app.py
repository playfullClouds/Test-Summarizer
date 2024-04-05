# import streamlit as st
# # Adjust the import path based on your project structure
# from textSummarizer.pipeline.prediction import PredictionPipeline

# # Initialize the prediction pipeline
# prediction_pipeline = PredictionPipeline()

# # Title for the app
# st.title('Test Summarizer App')

# # Text input for user to enter text to summarize
# user_input = st.text_area("Enter Text to Summarize", height=300)

# # Button to trigger summarization
# if st.button('Summarize'):
#     # Check if the user has entered some text
#     if user_input:
#         # Use the prediction pipeline to get the summary
#         summary = prediction_pipeline.predict(user_input)
#         # Display the summary
#         st.write("Summary:")
#         st.write(summary)
#     else:
#         st.write("Please enter some text to summarize.")




import streamlit as st
from src.textSummarizer.pipeline.prediction import PredictionPipeline

# Set page config to add a title and favicon (optional)
st.set_page_config(page_title="Test Summarizer", page_icon="📝", layout="wide")

# Custom CSS to hide the hamburger menu and the footer (possibly containing the deploy button)
hide_menu_style = """
           <style>
           #MainMenu {visibility: hidden;}
           .stDeployButton {display:none;}
           footer {visibility: hidden;}
           </style>
           """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Initialize the prediction pipeline
prediction_pipeline = PredictionPipeline()

# Use columns to organize content for better visual appeal
col1, col2 = st.columns(2)

with col1:
    # Title for the app
    st.title('Test Summarizer App')

    # Text input for user to enter text to summarize, with a larger area
    user_input = st.text_area("Enter Text to Summarize", height=300, placeholder="Paste your text here...")

    # Inside your Streamlit app, where you call the predict method
    if st.button('Summarize'):
        if user_input:
            # Dynamically set max_length based on the length of user_input
            input_length = len(user_input.split())  # Counting words in the input
            max_length = input_length  # Directly using input length as max_length
            
            # Now call predict with the dynamically determined max_length
            with st.spinner('Generating summary...'):
                summary = prediction_pipeline.predict(user_input, max_length=max_length)
            
            # Display the summary as before
            col2.subheader("Summary:")
            col2.write(summary)
        else:
            st.write("Please enter some text to summarize.")








