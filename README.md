# IHU EDA - Chatbot Backend

## Getting started

Requirements:
- NodeJS 10+
- Yarn 1.15+
- Angular CLI 7.3.8+
- Python 3.6+
- Pip

### 1. Cloning the projects

In order to get the project running you need to have the following folder structure:

```
- empty_folder/
    |
    |- eda-chatbot-frontend/
    |   Clone the project from: https://github.com/tomvlk/ihu-eda-chatbot-frontend.git with:
    |   git clone https://github.com/tomvlk/ihu-eda-chatbot-frontend.git eda-chatbot-frontend
    |
    |- eda-chatbot-backend/
    |   Clone the project from: https://github.com/tomvlk/ihu-eda-chatbot-backend.git with:
    |   git clone https://github.com/tomvlk/ihu-eda-chatbot-backend.git eda-chatbot-backend
```
This way the backend knows where the frontend dist folder is located.

*Command on linux to create this structure from the empty folder perspective (make sure you CD into the empty folder):*
```
git clone https://github.com/tomvlk/ihu-eda-chatbot-frontend.git eda-chatbot-frontend && git clone https://github.com/tomvlk/ihu-eda-chatbot-backend.git eda-chatbot-backend
```

### 2. Preparing Dialogflow project

1. Go to the Dialogflow site and create a new project. 
2. Download or locate the ZIP-file from the backend project (you already cloned this project).
3. Go the the Dialogflow Console and hit the Gear button on the left upper corner (just near the project name).
4. Hit the tab 'Export and Import'
5. Select the button 'Restore from ZIP' and select the previous located file.
6. Follow the steps on-screen to restore the predefined project into your Dialogflow account.
7. Enable the Dialogflow API. Follow this guide: https://medium.com/google-cloud/how-to-create-a-chatbot-using-dialogflow-enterprise-edition-and-dialogflow-api-v2-923f4a965176#fe15
8. Make sure you download the JSON file from the Google Cloud Console and put it in the `eda-chatbot-backend/` folder and name it `key.json`.

### 3. Prepare the frontend

1. Go to the frontend folder in your favourite command prompt console.
2. Install the dependencies with Yarn:  
    `yarn install`
3. Build the frontend with Angular CLI:  
    `ng build`
4. The frontend should be ready and build. You can test this by navigating to the `dist` folder in the frontend project folder.

### 4. Prepare the backend

1. Create a virtualenv in the backend folder with:  
    `virtualenv -p python3 env`  
    or on Windows: `virtualenv env` (make sure Python 3.6+ is installed as default on Windows).

2. Activate the virtualenv:  
    Linux: `source env/bin/activate`  
    Windows (Generic): `.\env\Scripts\activate.bat`  
    Windows (PowerShell): `.\env\Scripts\activate.ps1`
3. Install or update backend dependencies:  
    `pip install -r requirements.txt -U`

### Run the project

To run the project, make sure you are in the backend folder with an **activated virtualenv** and enter the following command:

`python run.py`
