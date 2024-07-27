# Phishing-Detector

## Objective:
The primary goal of this project is to build a machine learning model that can detect phishing emails. Phishing emails are fraudulent messages designed to trick recipients into providing sensitive information, and detecting them is crucial for cybersecurity.

## Project Structure:

data/
- CEAS_08.csv: The dataset containing email data used for training the model.

notebooks/
- phishing_detection.ipynb: A Jupyter notebook containing the entire workflow for data preprocessing, model training, evaluation, and saving the model.

src/: Source code for different parts of the project.
- __init__.py: Marks the directory as a Python package.
- data_preprocessing.py: Contains the function for preprocessing email text.
- model_training.py: Script for loading data, preprocessing, training the model, evaluating, and saving the model and vectorizer.
- utils.py: Utility functions (if needed).
- predict.py: Function for loading the model and vectorizer, and predicting if an email is phishing or not.
models/: Saved models.
- phishing_model.pkl: The trained phishing detection model.
- tfidf_vectorizer.pkl: The TF-IDF vectorizer used to transform email text data.
streamlit_app.py: Streamlit app script for deploying a web interface where users can input email text and get predictions.

requirements.txt: List of dependencies required for the project.

README.md: Project overview, setup instructions, and usage guide.

## Workflow:

1. Data Loading and Preprocessing:
The email data is loaded from CEAS_08.csv.
Emails are preprocessed using preprocess_email function to clean the text and remove stopwords.
2. Feature Extraction:
TF-IDF Vectorizer is used to convert the cleaned email text into numerical features suitable for machine learning.
3. Model Training:
A Naive Bayes classifier (MultinomialNB) is trained on the processed email data to distinguish between phishing and non-phishing emails.
4. Model Evaluation:
The model's performance is evaluated using accuracy and a classification report.
5. Model Saving:
The trained model and TF-IDF vectorizer are saved using joblib.
6. Streamlit Web Application:
A Streamlit app (streamlit_app.py) provides a user interface where users can enter the body of an email.
The app processes the input, uses the trained model to predict if the email is phishing, and displays the result.

## Setup

1. Clone the repository.
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

## Usage

- Open the Streamlit app in your browser.
- Enter the body of the email you want to check.
- Click the "Check" button to see if the email is a phishing email.
