# Phishing-Detector

## Objective:
The primary goal of this project is to build a machine learning model capable of detecting phishing emails. Phishing emails are fraudulent messages designed to trick recipients into providing sensitive information, and detecting them is crucial for cybersecurity.

## Demo:

https://github.com/user-attachments/assets/aa69e834-d0aa-4eb0-9321-58572130a998

## Key Features:
- Model Development: Developed a machine learning model to detect phishing emails with high accuracy.
- Frontend Implementation: Designed and implemented the front-end using the Streamlit framework to provide a user-friendly web interface for real-time email phishing detection.
- Data Preprocessing: Utilized Pandas and NLTK for data preprocessing, including tokenization, stopwords removal, and lemmatization.
- Feature Extraction: Employed TfidfVectorizer from Scikit-learn for feature extraction, converting email text into numerical data.
- Classification Model: Trained a Multinomial Naive Bayes classifier to classify emails as phishing or non-phishing.
- Performance Evaluation: Achieved high model performance, evaluated using accuracy score and classification report metrics.
- Model Management: Saved and managed the trained model and vectorizer using Joblib for future predictions.

## Project Components:

1. **Dataset**:
    - CEAS_08.csv: The dataset containing email data used for training the model.
    - Dataset Source: [Curated Dataset - Phishing Email](https://figshare.com/articles/dataset/Curated_Dataset_-_Phishing_Email/24899952?file=43817124)

2. **Notebook**:
    - preprocess.ipynb: A Jupyter notebook containing the entire workflow for data preprocessing, model training, evaluation, and saving the model.

3. **Models**:
    - phishing_model.pkl: The trained phishing detection model.
    - tfidf_vectorizer.pkl: The TF-IDF vectorizer used to transform email text data.

4. **App Script**:
    - app.py: Streamlit app script for deploying a web interface where users can input email text and get predictions.

5. **Documentation**:
    - README.md: Project overview, setup instructions, and usage guide.

## Workflow:

1. **Data Loading and Preprocessing**:
    - Load email data from CEAS_08.csv.
    - Preprocess emails using preprocess_email function to clean the text and remove stopwords.
2. **Feature Extraction**:
    - Use TF-IDF Vectorizer to convert the cleaned email text into numerical features suitable for machine learning.
3. **Model Training**:
    - Train a Naive Bayes classifier (MultinomialNB) on the processed email data to distinguish between phishing and non-phishing emails.
4. **Model Evaluation**:
    - Evaluate the model's performance using accuracy and a classification report.
5. **Model Saving**:
    - Save the trained model and TF-IDF vectorizer using Joblib.
6. **Streamlit Web Application**:
    - Develop a Streamlit app (app.py) providing a user interface where users can enter the body of an email.
    - The app processes the input, uses the trained model to predict if the email is phishing, and displays the result.

## Setup

1. Clone the repository.
2. Download the dataset and run preprocess.ipynb.
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

- Open the Streamlit app in your browser.
- Enter the body of the email you want to check.
- Click the "Check" button to see if the email is a phishing email.
