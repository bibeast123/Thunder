""" Contains recommendation class"""
from sklearn.neighbors import KNeighborsClassifier  # Import KNeighborsClassifier
from ...configs import *
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommendation:
    """class responsible for provding solutions given issues"""
    
    def __init__(self):
        pass
    
    @classmethod
    def recommend_solutions(cls):
        """gets solution to issues given summary and issues

        Returns:
            str: recommended solution
        """
        
        issue_solution_df = pd.read_csv(TRAINING_SOLN_PATH)
        predicted_issue_df = pd.read_csv(ISSUES_CSV_PATH)

        with open('./iic-group10/backend/db/created/summary_1.txt', 'r') as file:
            summary_text = file.read().strip()
        
        # Preprocess data
        predicted_issue_df['Summary'] = summary_text
        issue_solution_df['Combined'] = issue_solution_df['Issue'] + ' ' + issue_solution_df['Summary']
        predicted_issue_df['Combined'] = predicted_issue_df['Issue'] + ' ' + predicted_issue_df['Summary']
        
        # Cosine similarity
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(issue_solution_df['Combined'])
        predicted_issue_vec = tfidf_vectorizer.transform(predicted_issue_df['Combined'])
        cosine_similarities = cosine_similarity(predicted_issue_vec, tfidf_matrix).flatten()
        most_similar_index = cosine_similarities.argmax()
        recommended_solution = issue_solution_df.iloc[most_similar_index]['Solution']

        # Save amd return text
        with open(RECOMMENDED_SOLUTION_PATH, "w") as f:
            f.write(recommended_solution)
       
        print(recommended_solution)
        return recommended_solution
