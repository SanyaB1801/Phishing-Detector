# Phishing-Detector

This project uses machine learning to detect phishing emails.

## Project Structure

phishing_detector/
├── data/
│ └── CEAS_08.csv
├── notebooks/
│ └── phishing_detection.ipynb
├── src/
│ ├── init.py
│ ├── data_preprocessing.py
│ ├── model_training.py
│ ├── utils.py
│ └── predict.py
├── models/
│ ├── phishing_model.pkl
│ └── tfidf_vectorizer.pkl
├── streamlit_app.py
├── requirements.txt
└── README.md


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
