# QA-Core-Fundamental-Project
Repository for the DevOps Core Fundamental Project

## Table of Contents:
* [Project Brief](#Project-Brief)
* [Getting Started](#Getting-Started)
* [ERD](#ERD)
* [CI Pipeline](#ci-pipeline)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The Application](#The-Application)

## Project Brief
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. This can be seen in the screenshot below, which outlines the structure of the project. 
![Image showing the structure of the project](/README_Images/Project_design.drawio.png)

## Getting Started
The first step in starting this project was to decide on an idea for the project. 
The idea that I have decided to pursue is a **Film Review Application**. This web app will allow a user to select a movie from the list of movies available to review, and leave a text review, along with assigning it a star rating. These reviews will then be displayed for anyone that enter the website and selects that movie. 

The **Film Review Application** will have a **-One-to-Many-** relationship in the table and can also be extended to have a second intermediary table between the **Films table** and the **Reviewers table**. 

The **ERD** for this project and how it can also be extended further is shown below. 

## ERD
The ERD below outlines the relationship between the different tables in the database which the application will use, and how these tables will be setup. 
The first ERD shows the basic outline for the application. 
![Image showing ERD for first iteration of application](/README_Images/Project_ERD_Initial.png)

### Extended ERD
The second ERD shows how it can be extended to have the intermediary reviews table between the films and reviewers table.
 
![Image showing ERD for extended iteration of application](/README_Images/Project_ERD_Extended.png)

## CI Pipeline
Other than what was mentioned above, the project specification also required the implementation of some of the elements of a typical CI Pipeline. This included: project tracking, version control, development environment and build server. 

### Project Tracking
For project tracking, I used Trello in order to build a project tracking board. Each of the different tasks was added to the project backlog and during the course of the sprint, each item was moved from the backlog to in progress, to completed and finally to pushed to main once the task had been pushed to main on the Github repository. The board at the start of the project can be seen below:
![Image showing Trello board at the start of the project](/README_Images/Trello_Board_Start.png)
The following link will take you to the [Trello Board](https://trello.com/b/sUR77DK2/qa-core-fundamental-project) to view the full board. 

### Version Control
For Version Control, git was used. The repository for the project was hosted and stored on github. Version control allows for the recall of past work that has been completed and git has great integration within CI Pipelines and allows for easy creation through the feature-branch model for version control. To achieve this model of production, a new branch was created from the development branch for each of the different features that was being developed. Once these were fully functional, they could then be pull requested back to the development branch. Only once a "full version" of working code was stored within the development branch would a pull request be made to merge the changes back to the main (live environment) branch. 

By working in this way (with the feature branch model), it allowed for the project to progress and extended work be worked on without the risk of the live product breaking while attempting to extend the project further. The screenshot below shows the network diagram for the project, which outlines each of the different branches during the procution up to version 1.0 being deployed to main. 
![Image showing the network diagram](/README_Images/Project_Network_Graph_One.png)
![Image showing the network diagram](/README_Images/Project_Network_Graph_Two.png)

### Development Environment
The development environment which was used for the development of this project was python3 virtual environment (venv) which was hosted on a virtual machine running Ubunto Pro 20.04. Flask is a python based framework, and therefore python3 was required. The virtual environment allows for pip3 installs to be performed, so the virtual environment can run all of the required frameworks, such as Flask. This also means that there will be no conflicting installs when testing new software on the virtual environment as this will have different installs compared to the live environment. 

### Jenkins
Jenkins was used as a build server, which provided automation for building and testing the projects application. To achieve automation, a freestyle project was needed to be setup. This freestyle project executes the test.sh file when a webhook is recieved from github when pushing a commit to the Development branch. 

The full CI Pipeline can be seen in the diagram below:
![Image showing the full CI Pipline](/README_Images/CI_Pipeline_Diagram.drawio.png)

## Risk Assessment
The next step after deciding on the projects idea was to create a risk assessment. 
This is a table which outlines the possible risks to the project, the likelihood of the risk occuring, the impact the risk would have to the project, the control that will take place to minimise/reduce the risk and how frequent that control needs to be carried out. The table can be seen below:
![Image showing the Risk Assessment Table](/README_Images/Project_Risk_Assessment_Table.png)

## Testing
An essential part of the production of the application was testing the web app. The application being built is not a production application and therefore security testing was outside the scope for this project. However, if this was not the case security testing would have been performed on the application to ensure that it is secure both for the end users and from any malicious attacks such as a MITM, SQLInjection or DDOS attack. 

The testing that did take place however was the following:
* Unit testing: 
    * Unit tests were used for the applications functionality. They are used to test all of the different functions of the application. The unit tests that were written are able to test the **C**reate, **R**ead, **U**pdate and **D**elete (**CRUD**) functionality of the web application, ensuring it is all working as intended. 
* Integration testing:
    * Integration testing ...

All testing was performed automatically by using Jenkins via a github webhook. The screenshot below shows a log which is created after every Github webhook on the Jenkins server. 
![Image showing the webhook log on the Jenkins server](/README_Images/Jenkins_github_webhook_log.png)

The webhook was setup so that for every push and pull request to the Development branch triggered a build on Jenkins, which resulted in the tests (from the API pytest) being performed on the jenkins server. Everytime this Jenkins build was triggered and completed, a artifact was created which outputted the coverage report for the tests into a HTML page. The artifact can be seen on the Jenkins server in the screenshot below:
![Image showing the artifact that is created after a build is run](/README_Images/Jenkins_artifacts.png)

The following screenshot shows the coverage report HTML page which is created after every successful build:
![Image showing the html output of coverage report from pytest](/README_Images/Pytest_Coverage_report.png)

## The Application
The aim of the application is to build a **CRUD** (**C**reate, **R**ead, **U**pdate and **D**elete) application. The following outlines how each of these functions has been achieved within the application. 
### Create:
The create function of the application has three different functionalities, these being:
* Create a film
* Create a reviewer
* Create a review

#### Add Film:
The below screenshots shows how a film is created within the application:

![Adding a Film](/README_Images/Home_No_Entries.png)
![Adding a Film](/README_Images/Add_Film.png)
![Adding a Film](/README_Images/Add_film_w_Details.png)
![Adding a Film](/README_Images/Home_With_Film.png)

#### Add Reviewer:
The below screenshots shows how a reviewer is created and added to the database:

![Adding a Reviewer](/README_Images/Home_With_Film.png)
![Adding a Reviewer](/README_Images/Add_Reviewer.png)
![Adding a Reviewer](/README_Images/Add_Reviewer_w_Details.png)
![Adding a Reviewer](/README_Images/Home_With_Film_and_Reviewer.png)

#### Add Review:
The below screenshots shows how a review is created based on a reviewer and film:

![Adding a Review](/README_Images/Home_With_Film_and_Reviewer.png)
![Adding a Review](/README_Images/Add_Review.png)
![Adding a Review](/README_Images/Add_Review_W_Details.png)
![Adding a Review](/README_Images/Home_w_Film_Reviewer_Review.png)

### Read:
In order to read the data from the application which has been added, the user has a number of options. This being the home page, which displays the different films, reviewers and reviews which have been added to the application. This can be seen in the screenshot below:

![Reading the home page](/README_Images/Home_w_Film_Reviewer_Review.png)

Another way in which a user can read the data is by going to each of the different "View All X" pages, wherre X can be either: films, reviewers or reviews. The different pages can be seen in the screenshot below:

![Reading All Films](/README_Images/View_all_films.png)
![Reading All Reviewers](/README_Images/View_All_Reviewers.png)
![Reading All Reviewers](/README_Images/View_All_Reviews.png)


The final way in which a user can read the data, is by selecting to view all the reviews for any specific film. This is done through the view all films page, and selecting the film you would like to see all the reviews for. This can be seen in the screenshots below:

![Reading All Reviews for a Film page](/README_Images/View_All_Reviews_Specific_Film.png)
![Reading All Reviews for a Film page](/README_Images/View_All_Reviews_Specific_Film_2.png)


### Update:
A user is able to update any entry into the application. This can be a film, reviewer or review. Each are done in a similar way, in that there is a link displayed with each entry which allows the user to update the details. The screenshots below show the process of updating a film entry. 

![Updating a film](/README_Images/Update_Film_1.png)
![Updating a film](/README_Images/Update_Film_2.png)
![Updating a film](/README_Images/Home_w_Updated_Film.png)
The screenshot above shows the homepage with the updated film on it. 

### Delete:
A user is able to delete any entry into the application. This can be a film, reviewer or review. Each are completed in the same way, with a link being added next to each entry which is added to the application. When a user clicks on the delete button, the entry will be removed from the database and then will no longer be displayed on any of the pages. 

![Deleting Review](/README_Images/Delete_Review_1.png)
![Deleting Review](/README_Images/Home_w_Deleted_Review.png)

The screenshot above shows the home page with the now deleted review. 

![Deleting Review](/README_Images/View_All_Reviews_w_Deleted.png)

The screenshot above shows the view all reviews page with the review entry now deleted. 


