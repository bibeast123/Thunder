# Team 10 Customer is Always Right

## Project Summary

### Problem
> Based on customer reviews, we found that customers are being fed up with call times lasting
too long or reaching unsatisfactory conclusions on their call. We believe we can improve on
their experience.

### Goal
> Our project aims to assist call representatives with the goal to better enhance, improve, and
personalize how customers interact with our call representatives (digital interaction).

### Solution
> Analyze call transcripts and use some form of ML/AI to better analyze the issue customers
are facing. Using their profile information, and previous call records, we can analyze in real
time the issues a customer my face and swiftly find solutions, effectively, reducing customer
impatience and reaching a definitive conclusion

## Frontend GUI

![](/images/gui-frontend.png)


## Backend GUI

![](/images/gui-backend.png)


## Frontend Design Document

![](/images/frontend-design.png)


## Backend Design Document

![](/images/backend-design.png)


## Prerequisites
- Python
- Node.js
- Code editor
- Windows
- Proxy Setup

### Proxy Setup
You need to make sure you have you proxy setup; most issues arrise from an improperly configured proxy. Run these in in the CMD anywhere in the project:
1. `npm config set proxy http://cso.proxy.att.com:8888`
2. `npm config set https-proxy http://cso.proxy.att.com:8888`
3. `npm config set registry http://registry.npmjs.org/`
4. `npm config set strict-ssl false`



## How To Run

### Cloning the repository
1. If you're a developer, you need to have Git access: https://att.sharepoint.com/sites/DevOpsCICD/SitePages/Proxy-Setup.aspx#instructions-for-git-bash
2. Clone the repository once your GIT works.
3. Make sure the repository is cloned in a safe place, for example: `C:\Users\<att id>\dev\<repo>`

### Getting Python env setup
1. Open Vscode or any code editor and then navigate to the terminal
2. Create a virtual environment inside the cloned repo: `users/<userid>/repo/iic-group10> py -3 -m venv .venv`
3. Activate your virtual environment: `.venv\scripts\activate`
4. Install from the req doc: `python -m pip install -v --no-build-isolation --timeout=1000 --default-timeout=100 -v --proxy http://cso.proxy.att.com:8888 --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt`
5. Install the punctuation module: `python -m pip install -v --timeout=1000 --default-timeout=100 -v --proxy http://cso.proxy.att.com:8888 --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org deepmultilingualpunctuation`
6. Install the speech to text module: `python -m pip install -v --no-build-isolation --timeout=1000 --default-timeout=100 -v --proxy http://cso.proxy.att.com:8888 --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org vosk`
7. Create the users in the database: `python -m iic-group10.backend.scripts.create_users`
8. Verify the backend setup works: `python -m iic-group10.backend.app`
9. End flask by entering `CTRL + C`
10. You can deactivate your virtual environment with the command: `deactivate`.

### Installing the language Model
In the project directory, you need to install the language model used and unzip it:
1. `curl --compressed -O --ssl-no-revoke --proxy  "http://cso.proxy.att.com:8888" "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"`
2. `tar -xf vosk-model-small-en-us-0.15.zip`
3. `del /f vosk-model-small-en-us-0.15.zip"`

### Starting the frontend
Open a CMD and run the following commands to start your front end:
1. `npm install --fetch-timeout=60000`
2. `npm run dev`

### Starting the backend
1. Perform a `cd ..` so that you are onestep above the repository location.
2. Ecample: `(.venv) C:\Users\<att id>\dev`
3. You should also create the users from the csv before running any api endpoints. You can do this by running: `python -m iic-group10.backend.scripts.create_users`
4. Start the Flask app with: `python -m iic-group10.backend.app`
5. End flask by entering `CTRL + C`
6. You can deactivate your virtual environment with the command: `deactivate`.


## Contributors
- Devkota Bidhan (dev)
- Nguyen Jason (dev)
- Hogan-Bailey Aman (dev)
- Randhawa Omer (dev)
- Kwon Daewon (dev)
- Janssen Trevor (prjmt)


