""" module creates users inside of db from a csv"""
import csv
import json
from ..app import app, db, User
import os

os.chdir('iic-group10/backend/')
print(os.getcwd())

def create_users_from_csv(csv_file_path):
    """Creates new users into a db from a csv

    Args:
        csv_file_path (str): path to csv
    """
    try:
        with open(csv_file_path, newline='') as csvfile:
            # Debug: Check and print file contents
            file_contents = csvfile.read()
            print("File Contents:\n", file_contents)
            
            # Move the file pointer back to the beginning of the file
            csvfile.seek(0)

            reader = csv.DictReader(csvfile)
            rows = list(reader)

            # Debug: Print number of rows read
            print("Number of rows read:", len(rows))

            for row in rows:
                try:
                    # Debug: Print each row from the CSV
                    print("CSV Row:", row)

                    # Fix JSON fields by replacing single quotes with double quotes
                    preferences = json.loads(row['preferences'].replace("'", '"'))
                    previous_calls = json.loads(row['previous_calls'].replace("'", '"'))
                    accounts = json.loads(row['accounts'].replace("'", '"'))

                    # Create User object
                    user = User(
                        firstname=row['firstname'],
                        lastname=row['lastname'],
                        email=row['email'],
                        preferences=preferences,
                        previous_calls=previous_calls,
                        accounts=accounts,
                        audio_path=row['audio_path'],
                        transcript_path=row['transcript_path'],
                        sol_path=row['sol_path'],
                        category_path=row['category_path'],
                        summary_path = row['summary_path']
                    )

                    # Debug: Print User object
                    print("User Object:", user)
                    
                    db.session.add(user)
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON for row {row}: {e}")
                    exit(-1)
                except KeyError as e:
                    print(f"Missing expected field {e} in row {row}")
                    exit(-1)
                except Exception as e:
                    print(f"Unexpected error for row {row}: {e}")
                    exit(-1)

            db.session.commit()
            print("Users created successfully from CSV!")

    except FileNotFoundError as e:
        print(f"File not found: {csv_file_path}")
    except Exception as e:
        print(f"Error reading file {csv_file_path}: {e}")

# Run this script
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the database and tables are created
        create_users_from_csv(str(os.path.dirname(os.path.realpath(__file__))) + '/users.csv')
