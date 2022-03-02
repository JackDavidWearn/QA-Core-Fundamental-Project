# QA-Core-Fundamental-Project
Repository for the DevOps Core Fundamental Project

## Table of Contents:
* [Project Brief] (#project-brief)
* [Getting Started] (#Getting-Started)
* [ERD] (#ERD)
* [Extended ERD] (#Extended-ERD)
* [Risk Assessment] (#Risk-Assessment)

## Project Brief
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship.

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

## Risk Assessment
The next step after deciding on the projects idea was to create a risk assessment. 
This is a table which outlines the possible risks to the project, the likelihood of the risk occuring, the impact the risk would have to the project, the control that will take place to minimise/reduce the risk and how frequent that control needs to be carried out. The table can be seen below:
![Image showing the Risk Assessment Table](/README_Images/Project_Risk_Assessment_Table.png)


