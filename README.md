# LogoAITest
This Repo is create as per the discussion on June 6th (Firday) with Jhonatan Oliverira

In this repo I will use python to:
- Call to an API
- Recieve data
- Save data in firebase
- Assert data is saved as expected

Optionaly:
- upload python function to google cloud function

Plan: 
1st Python function
* call API and receive data (Fake API: https://jsonplaceholder.typicode.com)
* Save data in Firestore (db in Firebase)


2nd Python function
* Calls 1st function
* Assert data is saved as expected

3rd Github Repo
* Create a Github repo

3rd Upload both to Google Cloud Functions
* Upload the Python function to Google Cloud Functions


06/12/2023 6:57pm
- Can get data from JASONplaceholder.com
- Can write to firebase
Next Step
- [Done] Change file name from __init--.py to __initi__py
- [Done] Relocate security key from desk top download to firebaseServiceAccountKey.json
- [Done] Refector getFakeData to independent function
- [Done] Seperate function and file more apporopreately
Next step on Feature
- [Done] Connect fake data to database

0613/2023 12:12pm
- Problem: relative path to firebaseServiceAccountKey.json not valid. I found out that In python, relative paths are resolved based on the current working directory. which means depending on the directory you run the function from, the relative path changes.
  Solution: https://towardsthecloud.com/get-relative-path-python#:~:text=A%20relative%20path%20starts%20with,path%20to%20the%20file%20want.
  use os to find absolut path.
  
- Can retrieve data from firebase

***Don't forget to "source logoAITest/bin/activate" You can get out by "deactivate"

To Run app:
  1 clone repo
  2 create a "firebaseServiceAccountKey.json" file and paste firebase credential
  3 run terminal command "source logoAITest/bin/activate"
  4 run python3 app.py
    you should see a "pass" print out in the terminal the data writen in the firestore


