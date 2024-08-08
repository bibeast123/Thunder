"""Business logic module and interacts with the database"""

from ...configs import *
from ..helpers.trascriber import *
from ..ml.summarize import *
from ..ml.categorizer import Categorizer
from ..ml.recommendations import Recommendation
from ..helpers.logger import logData


def update_user(db, User, user_id, request):
    """Updates a user in the database

    Args:
        db (db): database
        User (db.Model): database Model
        user_id (int): user id
        request (json): request

    Returns:
        {} or {}, int: response
    """
    
    user = User.query.get(user_id)
    
    if not user:
        return {'message': 'User not found'}, 404
    
    data = request.json

    if 'firstname' in data:
        user.firstname = data['firstname']
    if 'lastname' in data:
        user.lastname = data['lastname']
    if 'email' in data:
        user.email = data['email']
    if 'preferences' in data:
        user.preferences = data['preferences']
    if 'previous_calls' in data:
        user.previous_calls = data['previous_calls']
    if 'accounts' in data:
        user.accounts = data['accounts']
    if 'audio_path' in data:
        user.audio_path = data['audio_path']
    if 'transcript_path' in data:
        user.transcript_path = data['transcript_path']
    if 'sol_path' in data:
        user.sol_path = data['sol_path']
    if 'category_path' in data:
        user.category_path = data['category_path']
    if 'summary_path' in data:
        user.summary_path = data['summary_path']
    
    user.updated_at = db.func.now()
    db.session.commit()
    return {'message': f'User {user_id} updated successfully'}

def get_user(User, user_id):
    """Gets a user in the database

    Args:
        User (db.Model): database Model
        user_id (int): user id

    Returns:
        {} or {}, int: response
    """
        
    user = User.query.get(user_id)

    if not user:
        return {'message': 'User not found'}, 404
    
    logData(f'Succesfully got user {user.firstname}')
    return { 
        'id': user.id, 'firstname': user.firstname, 'lastname': user.lastname, 'email': user.email, 
        'preferences': user.preferences, 'previous_calls': user.previous_calls,
        'accounts': user.accounts, 'audio_path': user.audio_path,
        'transcript_path': user.transcript_path, 'sol_path': user.sol_path, 'category_path': user.category_path,
        'created_at': user.created_at, 'updated_at': user.updated_at, 'summary_path':user.summary_path
    }
        
def get_users(User):
    """Gets a list of users

    Args:
        User (db.Model): db Model

    Returns:
        {} or {}, int: response
    """
    users = User.query.all()
    return [ 
        {'id': user.id, 'firstname': user.firstname, 'lastname': user.lastname,
            'email': user.email, 'preferences': user.preferences, 'previous_calls': user.previous_calls,
            'accounts': user.accounts,'audio_path': user.audio_path,
            'transcript_path': user.transcript_path, 'sol_path': user.sol_path, 'category_path': user.category_path,
            'created_at': user.created_at, 'updated_at': user.updated_at, 'summary_path':user.summary_path
        } for user in users
    ]

def delete_users(db, User):
    """Deletes all users in the db

    Args:
        db (db): database
        User (db.Model): database Model

    Returns:
        {} or {}, int: response
    """
    
    try:
        num_deleted = db.session.query(User).delete()
        db.session.commit()
        return {'message': f'{num_deleted} users deleted successfully'}
    
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500
    
def delete_user(db, User, user_id):
    """Deletes a user in the database

    Args:
        db (db): database
        User (db.Model): database Model
        user_id (int): user id

    Returns:
        {} or {}, int: response
    """

    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    
    db.session.delete(user)
    db.session.commit()
    logData(f'Successfully deleted user: {user.firstname} ')
    return {'message': f'User {user_id} deleted successfully'}

def get_transcription(User, user_id):
    """Creates transcription for a user

    Args:
        User (db.Model): database model
        user_id (int): user id

    Returns:
        {} or {}, int: response
    """
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    
    transcription = ''
    try:
        with open(user.summary_path, 'r') as f:
            transcription = f.read()
            logData('Transcription already exists')
    except:
        transcription = transcribe_audio(user.audio_path,  user.transcript_path)

    
    logData(f'Successfully got a transcription for {user.firstname} at path {user.transcript_path}')

    return {"status": "success", transcription: "Data received"}, 200

def get_summary(User, user_id):
    """Creates a summary of the transcription

    Args:
        User (db.Model): database Model
        user_id (int): user id

    Returns:
        {}, int: response
    """
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    
    summary_text = ''
    try:
        with open(user.summary_path, 'r') as f:
            summary_text = f.read()
            logData('Summary already exists')
    except:
        summary_text =  create_summary(user.transcript_path, user.summary_path)
        logData('Created new summary')

    logData(f'Successfully got a summary for {user.firstname} at path {user.sol_path}')
    return {"status": "success", "summary": summary_text}, 200

def categorize(User, user_id):
    """Should either create or retireve analysis

    Args:
        User (db.Model): database Model
        user_id (int): user id

    Returns:
        {}, int: response
    """
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    
    issue = ''
    urgency = ''
    try:
        with open(user.category_path, 'r') as f:
            issue = f.read()
            logData('Caletgories already exists')

        with open('./iic-group10/backend/db/created/urgency.txt', 'r') as f:
            urgency = f.read()
            logData('Urgency already exists')
    except:
        urgency, issue = Categorizer.categorize_summary()
        logData('Created solutions')
    
    
    logData(f'Successfully got categories for {user.firstname} at path {user.category_path}')
    return {"status": "success", "urgency": urgency,  "issue": issue}, 200


def get_solutions(User, user_id):
    """Should either create or retrieve recommendation

    Args:
        User (db.Model): database Model
        user_id (int): user id

    Returns:
        {}, int: response
    """
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    

    solutions = ''
    try:
        with open(user.sol_path, 'r') as f:
            solutions = f.read()
            logData('solutions already exists')
    except:
        solutions =  Recommendation.recommend_solutions()
        logData('Created solutions')
    
    logData(f'Successfully got solutions for {user.firstname} at path {user.sol_path}')
    return {"status": "success", "solutions": solutions}, 200