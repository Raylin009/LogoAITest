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
- Change file name from __init--.py to __initi__py
- Relocate security key from desk top download to firebaseServiceAccountKey.json
- Refector getFakeData to independent function
- Seperate function and file more apporopreately
Next step on Feature
- Connect fake data to database

***Don't forget to "source logoAITest/bin/activate" You can get out by "deactivate"