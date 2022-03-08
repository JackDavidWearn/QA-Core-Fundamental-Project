# QA-Core-Fundamental-Project
Repository for the DevOps Core Fundamental Project

## Table of Contents:
* [Project Brief](#Project-Brief)
* [Getting Started](#Getting-Started)
* [ERD](#ERD)
* [CI Pipeline](#ci-pipeline)
* [Risk Assessment](#Risk-Assessment)

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


