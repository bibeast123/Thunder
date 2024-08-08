""" Contains categorization class"""
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import os
from ..helpers.logger import logData
from ...configs import *

class Categorizer():
    """responsible for categorizing data"""

    def __init__(self):
        pass
    
    @classmethod
    def predict_urgency_and_issue(cls, text, vectorizer, model_urgency, model_issue):
        """predicts issues given summary amnd urgency

        Args:
            text (str): summary text
            vectorizer (CountVectorizer): vectorizer
            model_urgency (KNeighborsClassifier): model
            model_issue (KNeighborsClassifier): model

        Returns:
            str,str: urgency,issue
        """

        text_vec = vectorizer.transform([text])
        prediction_urgency = model_urgency.predict(text_vec)
        prediction_issue = model_issue.predict(text_vec)

        urgency = 'High' if prediction_urgency[0] == 1 else 'Not High'
        issue_type = ISSUE_MAPPING[prediction_issue[0]]

        return urgency, issue_type

    @classmethod
    def categorize_summary(cls):
        """categorizes the summary by urgency and issue

        Returns:
            str,str: issue,urgency
        """
        
        # Check to see if the training data exists
        try:
            df = pd.read_csv(PATH_CATEGORY_TRAIN)
        except FileNotFoundError:
            print(NO_CSV_ERROR)
            exit()

        model_urgency = None
        model_issue = None
        vectorizer = CountVectorizer()

        urgency_model_path = URGENCY_MODEL_PATH
        issue_model_path =  ISSUE_MODEL_PATH
        vectorizer_path = VECTORIZER_PATH

        # Check if models already exist
        if os.path.exists(urgency_model_path) and os.path.exists(issue_model_path) and os.path.exists(vectorizer_path):
            with open(urgency_model_path, "rb") as file:
                model_urgency = pickle.load(file)
            with open(issue_model_path, "rb") as file:
                model_issue = pickle.load(file)
            with open(vectorizer_path, "rb") as file:
                vectorizer = pickle.load(file)

            logData("Models and vectorizer loaded from pickle files.")

        # If models do not exist, create them
        else:
            df['urgent_score'] = df['Urgency'].apply(lambda x: 1 if x == 'High' else 0)
            df['issue_score'] = df['Issue'].apply(lambda x: ISSUE_LABELS.index(x))

            X_train, X_test, y_train_urgency, y_test_urgency = train_test_split(
                df['Summary'], df['urgent_score'], test_size=0.2, random_state=42)
            _, _, y_train_issue, y_test_issue = train_test_split(
                df['Summary'], df['issue_score'], test_size=0.2, random_state=42)

            vectorizer = CountVectorizer()
            X_train_vec = vectorizer.fit_transform(X_train)

            model_urgency = KNeighborsClassifier(n_neighbors=5)
            model_urgency.fit(X_train_vec, y_train_urgency)

            model_issue = KNeighborsClassifier(n_neighbors=5)
            model_issue.fit(X_train_vec, y_train_issue)

            # Save models and vectorizer
            with open(urgency_model_path, 'wb') as f:
                pickle.dump(model_urgency, f)
            with open(issue_model_path, 'wb') as f:
                pickle.dump(model_issue, f)
            with open(vectorizer_path, 'wb') as f:
                pickle.dump(vectorizer, f)
            
            logData("Models and vectorizer trained and saved to pickle files.")


        with open(SUMMARY_PATH, "r")as f:
            summary = f.read()

        predicted_urgency, predicted_issue = cls.predict_urgency_and_issue(summary, vectorizer, model_urgency, model_issue)
        
        with open(ISSUES_CSV_PATH, "w")as f:
            f.write(f'Urgency,Issue\n')
            f.write(f'{predicted_urgency},{predicted_issue}\n')

        with open(ISSUES_TXT_PATH, "w")as f:
            f.write(f'{predicted_issue}\n')

        with open(URGENCY_PATH, "w")as f:
            f.write(f'{predicted_urgency}\n')

        logData(f"Predicted issue and urgency: {predicted_issue} , {predicted_urgency}")
        return (predicted_urgency, predicted_issue)