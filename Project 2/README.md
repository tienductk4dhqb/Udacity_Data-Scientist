# Data-Scientist-Project-2
## Disaster Response Pipeline Project
## Project Detail
In the Project, have a data set containing real messages that were sent during disaster events.  
You will be creating a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency.  
The project will include a web app where an emergency worker can input a new message and get classification results in several categories.  
The web app will also display visualizations of the data.  
This project will show off your software skills, including your ability to create basic data pipelines and write clean, organized code!  

![alt text](https://github.com/tienductk4dhqb/Data-Scientist-Project-2/blob/main/IMG/img1.png)  
![alt text](https://github.com/tienductk4dhqb/Data-Scientist-Project-2/blob/main/IMG/img2.png)  
![alt text](https://github.com/tienductk4dhqb/Data-Scientist-Project-2/blob/main/IMG/img3.png)  
### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage
## Structure Folder And File In Project
1. IMG  **Folder Image**
   1.1: img1.png  
   1.2: img2.png  
   1.3: img3.png  
2. app  
   2.1: templates  **Folder contains file display on FE.**  
       2.1.1: go.html  **Classification result page of web app.**  
       2.1.2: master.html  **Main page of web app.**  
   2.2: run.py  **Flask file that runs app.**  
3. data  **ETL: data pipeline is the Extract, Transform, and Load process.**  
   3.1: DisasterResponse.db  **The file stores data after cleaning.**  
   3.2: disaster_categories.csv  **The file contains categories type data.**  
   3.3: disaster_messages.csv  **The file contains message data.**  
   3.4: process_data.py  **File coding for ETL.**  
4. models  
   4.1: classifier.pkl  **Saved model**  
   4.2: train_classifier.py **Split the data into a training set and a test set.**   
   
