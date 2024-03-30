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

    # Button to trigger summarization
    if st.button('Summarize'):
        # Check if the user has entered some text
        if user_input:
            # Use the prediction pipeline to get the summary
            with st.spinner('Generating summary...'):
                summary = prediction_pipeline.predict(user_input)
            # Display the summary in the second column for a clear separation of input and output
            col2.subheader("Summary:")
            col2.write(summary)
        else:
            st.write("Please enter some text to summarize.")






