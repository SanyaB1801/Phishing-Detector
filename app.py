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
st.title('Phishing Email Predictor')

email = st.text_area('Enter the email content here:')
if st.button('Predict'):
    if email:
        email_preprocessed = preprocess_email(email)
        email_vectorized = vectorizer.transform([email_preprocessed])
        prediction = model.predict(email_vectorized)
        result = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
        st.write(f'The email is: {result}')
    else:
        st.write('Please enter email content')
