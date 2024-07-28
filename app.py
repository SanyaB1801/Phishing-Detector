import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.data.path.append('./nltk_data')

# Load the trained model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Define the preprocess_email function (ensure this is defined appropriately)
def preprocess_email(email):
    # Remove HTML tags
    email = re.sub(r'<.*?>', '', email)
    # Remove punctuation and numbers
    email = re.sub(r'[^a-zA-Z\s]', '', email)
    # Convert to lowercase
    email = email.lower()
    # Tokenize
    tokens = word_tokenize(email)
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Streamlit app
st.set_page_config(page_title='Phishing Email Predictor', page_icon=':email:', layout='wide')

# CSS styles
st.markdown("""
    <style>
    .main {
        background-color: #E0F7FA;
    }
    .sidebar .sidebar-content {
        background-color: #B2EBF2;
    }
    .stButton>button {
        background-color: #80DEEA;
        color: #006064;
    }
    .stTextArea>div>div>textarea {
        background-color: #E0F7FA;
        color: #006064;
        border: 2px solid #006064;
    }
    .stMarkdown {
        color: #006064;
    }
    .css-18e3th9 {
        background-color: #006064;
        color: white;
    }
    .css-1d391kg {
        background-color: #006064;
    }
    .css-1lcbmhc {
        color: #006064;
        background-color: #E0F7FA;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.header('Phishing Email Predictor')
st.sidebar.write('Enter the email content in the text box below and click Predict to check if the email is a phishing attempt.')

st.title('Phishing Email Predictor')
st.markdown('<p style="color:#006064;">This app uses a machine learning model to predict whether an email is a phishing attempt or not.</p>', unsafe_allow_html=True)

st.image("https://www.publicdomainpictures.net/en/view-image.php?image=585976&picture=mail-phishing", use_column_width=True)  # Adding an image for visual appeal

st.subheader('Instructions:')
st.markdown("""
1. Enter the email content in the text area below.
2. Click the **Predict** button to analyze the email.
3. The result will be displayed below.
""")

email = st.text_area('Enter the email content here:', height=250, placeholder='Type the email content here...')

if st.button('Predict'):
    if email:
        with st.spinner('Analyzing...'):
            email_preprocessed = preprocess_email(email)
            email_vectorized = vectorizer.transform([email_preprocessed])
            prediction = model.predict(email_vectorized)
            result = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
        st.success(f'The email is: **{result}**')
    else:
        st.error('Please enter email content')

st.sidebar.markdown('### About')
st.sidebar.info('This app is designed to help identify phishing emails using natural language processing and machine learning techniques.')

st.sidebar.markdown('### Contact')
st.sidebar.info('For more information or feedback, please contact us at support@example.com.')
