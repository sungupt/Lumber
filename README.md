# Lumber
## Lower Back Pain Predictor using Machine Learning and Data Science
### Objective
The main aim of this project is to detect the result of lumber- lower back pain
report data and apply logistics regression on data to predict whether the report
is normal or abnormal.
### Requirements
|  Software Needed |
|---------------------------------------------------------------------------------------------------------|
| Anaconda(Jupyter Notebook)                                                                              |
| Visual Studio Code or any Editor                                                                        |
| Frontend - A webpage to display predicted results using HTML, Cascading Style Sheet(CSS) and JavaScript |
| Python flask server for backend                                                                         |
 
### Analysis & Interpretation-

#### 1)Data Collection and dataset formation- 
Since,we needed a good quality data for our project,using which we can form our dataset for data modeling.We collected our data form Kaggle,and from various hospital patients’ report of there lower back pain.We collected our needed data from these reports,which was essential for our project.It was quite a tedious task. Then we form a dataset using MS Excel datasheet formation to form a datasheet.Still some data cleaning remains to be filtered out from the dataset.  

#### 2)Data Cleaning & Data Modelling-
To use the dataset for proper functioning of our project,firstly we need to clean the dataset from unwanted gaps to be removed from the dataset,which later helps in increasing the accuracy predicting the information taken from the user.For data cleaning,we upload the dataset in Jupyter Notebook,then use Numpy and pandas,libraries of python, to clean the dataset and to form a numeric data model.

a)Uploading Datasheet-
 

b)Using Numpy and pandas libraries for data cleaning & data modelling-
 
##### Data Cleaning- 
![image](https://github.com/sungupt/Lumber/assets/49180136/aaaca843-b574-4bc0-8173-e73938db69a3)
 
##### Data Modelling- 
![image](https://github.com/sungupt/Lumber/assets/49180136/a1f766f6-7799-4b60-ae98-affc8e657717)

 
#### 3)Data Visualization-
Visualization of data is necessary to perform operations on bulk datasets,so we use “Matplotlib” a library of python in Jupyter Notebook to visualise datas
stored to form data models.

Visualization of Lumbar datasheet-
![image](https://github.com/sungupt/Lumber/assets/49180136/9a0a0a00-fa30-45eb-8bc4-9679107c17bf)

  
#### 4)Forming data clusters to predict the patient’s report result-
Here,we use logistic regression,a machine learning algorithm, to segregate the data into clusters.The logistic regression method observes the datasets of lumbar pain,and forms two types of clusters which give a binary output as “Yes” or “No”.The clustering we used,provided in 87%-90% accuracy in predicting the test results.
a)No represent that the report is Normal
b)Yes represent that the report is  Abnormal
Formulae For Binary Cluster Formation-
                               
                                         F(x) =        L/(1+e^(-K(x-x0))

F(x)= Cluster function
L= Maximum Logistic Value
-K(x-x0)= Logistic Growth
x0= Value of sigmoid points

![image](https://github.com/sungupt/Lumber/assets/49180136/2eab14de-ba92-4434-a2c8-c33d6d8a3603)

 
#### 5)UI(User Interface) for entering patient report’s data-
We have made a user interactive,easy to use,web based app where any patient can enter their lumbar report’s data and detect their report’s result by clicking on the “Predict” button and can easily know their result.

a)Frontend- The frontend of the web app is made using simple html,css and javascript and a json file to accept inputs.Codes and tests are already shown in the coding & testing column.
![image](https://github.com/sungupt/Lumber/assets/49180136/280f5f2f-dddc-4f04-847d-276bb866eb92)

b)Backend server - The backend server of the web app is developed using “Python Flask”.Flask is a lightweight server side python platform that allows one to develop web applications.Flask uses a python based library ‘SKLearn’ to create requests and send to Jupiter's data model and is also cable of receiving data from UI,where user feeds the report’s data through json file format which interact with the flask server at local port: 8800.
Here once data is fed in the web UI,json make a request to server and sends data to server to detect the outcome.Server receives the data and send data to Jupyter’ data model where data is being processed and a prediction on that data is made.The the data model sends this predicted reply to server.Now server sends this data back to web UI,where the predicted data of the patient lumbar report’s result will be shown.
If Normal predicted,your report is negative. And if Abnormal predicted ,your result is positive and you need to consult a doctor.  

### References
https://www.kaggle.com/sammy123/lower-back-pain-symptoms-dataset 
