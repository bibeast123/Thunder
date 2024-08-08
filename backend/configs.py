"""list of global configurations"""

HTTP_PROXY="http://cso.proxy.att.com:8888"
"""ATTS http proxy"""

HTTPS_PROXY="http://cso.proxy.att.com:8888"
"""ATTs https proxy"""

PROXIES={"http" : HTTP_PROXY, "https" : HTTPS_PROXY}
"""dict of proxies"""

HEADERS={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
"""Required headers to bypass bot-preventions"""

BASIC_TEST_URL = "https://www.highspeedinternet.com/providers/att/reviews"
"""Test url to use"""

REVIEW_DB_NAME = './iic-group10/backend/db/reviews/reviews.csv'

REVIEW_SENT_ANALYSIS_NAME = './iic-group10/backend/db/analysis/review_sent_analysis.csv'

DB_BASE_DIR = './iic-group10/backend/db/analysis'

audio_path = './iic-group10/backend/db/test_call.wav'

TRANSCRIPTIONS_PATH = './iic-group10/backend/db/transcription.txt'

SCORES_PATH = './iic-group10/backend/db/scores.txt'

MODEL_PATH = './iic-group10/vosk-model-small-en-us-0.15'

LOG_FILE_PATH = './iic-group10/backend/db/log.txt'

USER_PROFILE = {
    "user_id": "user123",
    "first_name": "John",
    "last_name": "Doe",
    "number_of_previous_calls": 5,
    "list_of_preferences": ["Email", "SMS", "Push Notification"],
    "account_creation_date": "2023-01-15",
    "last_login_date": "2023-06-20",
    "email": "john.doe@example.com",
    "membership_level": "Gold",
    "age": 28,
    "location": {
        "country": "USA",
        "state": "California",
        "city": "San Francisco"
    }
}
PATH_CATEGORY_TRAIN = './iic-group10/backend/db/training/categ_train.csv'

BASE_ENDPOINT_STRING = """ <h1> List of API endpoints </h1>
<h2> User Apis </h2>
<ul>
<li> <a href="http://127.0.0.1:5000/users"> List all users </a> </li>
<li> <a href="http://127.0.0.1:5000/users/1"> Get user with id of one </a> </li> 
</ul>
<h2> ML Aps's </h2>
<ul>
<li> <a href="http://127.0.0.1:5000/ml/transcribe/1"> Transcribe audio of user with id of 1 </a> </li>
<li> <a href="http://127.0.0.1:5000/ml/summary/1"> Summarize data with of user with id of 1 </a> </li>
<li> <a href="http://127.0.0.1:5000/ml/categorize/1"> Categorize summary of user with id of 1 </a> </li>
<li> <a href="http://127.0.0.1:5000/ml/solutions/1"> Get solutions for user with id of 1 </a> </li>
</ul>
"""

ISSUE_MAPPING = {
    0: 'Internet Connectivity',
    1: 'Cable TV',
    2: 'Router or Modem',
    3: 'Phone Service',
    4: 'Device Troubleshooting',
    5: 'Disputing and Billing',
    6: 'Updating Information',
    7: 'Promotions',
    8: 'Upgrade Service',
    9: 'Feedback',
    10: 'Technician'
}


ISSUE_LABELS = [
       'Internet Connectivity', 'Cable TV', 'Router or Modem', 'Phone Service', 'Device Troubleshooting',
    'Disputing and Billing', 'Updating Information',
    'Promotions', 'Upgrade Service', 'Feedback', 'Technician'
]

NO_CSV_ERROR = "CSV file not found. Please check the file path."



URGENCY_MODEL_PATH = "./iic-group10/backend/db/models/model_urgency.pkl"
ISSUE_MODEL_PATH = "./iic-group10/backend/db/models/model_issue.pkl"
VECTORIZER_PATH = "./iic-group10/backend/db/models/vectorizer.pkl"
SUMMARY_PATH = "./iic-group10/backend/db/created/summary_1.txt"

ISSUES_CSV_PATH = "./iic-group10/backend/db/created/issues.csv"
ISSUES_TXT_PATH = "./iic-group10/backend/db/created/issues.txt"
URGENCY_PATH = "./iic-group10/backend/db/created/urgency.txt"

TRAINING_SOLN_PATH = './iic-group10/backend/db/training/soln_train.csv'
RECOMMENDED_SOLUTION_PATH = "./iic-group10/backend/db/created/solutions_1.txt"
