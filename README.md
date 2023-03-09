#SUVARNA SAHU CUBES PROJECT
Name : SUVARNA SAHU


This is a repository for all the sprints of software engineering course at Bridgewater State University.
Repository Structure:





**SPRINT 1 - Create a wufoo form and access the data using API**



MY WUFOO FORM LINK

https://ssahu.wufoo.com/forms/mxys8nv044etu7/


PROJECT REQUIREMENTS

Install Python and import packages-urllib,requests,json, 



PROJECT DESCRIPTION:
The project has three parts, In the first part I have created a wufoo form from the wufoo website. In the second part I have retrieved the data from the form through API key. In the third part I have created a output file, which automatically creates a file of the entries.



a brief description of what is missing from the project (if anything) - None from the given.


**SPRINT1-DONE**




**SPRINT 2-Saving the Wufoo Entries data to a database**


 MY WUFOO FORM LINK:
 https://ssahu.wufoo.com/forms/mxys8nv044etu7/


PROJECT REQUIREMENTS
Install Python and import packages json,sqlite3 
install packages
requests~=2.28.2
schedule~=1.1.0
APScheduler~=3.10.0
fastapi~=0.90.1
uvicorn~=0.20.0



PROJECT DESCRIPTION
In this sprint, I have created a database which stores the values of the form entries in the form of table. 
The records are inserted based on user entries.



TEST CASES



testcountcheck.py
the first automated test checks retrieves the data from the web and assures that we get the right number of data items.



testcreation.py
the second automated test creates a new empty database, run table creation function/method and then save data to database method and then checks to see that the database contains the test entry that we put in.




a very brief discussion of database layout and the table(s)- I have created 6 functions.



getentries(uri):
    fetch entries from the wufoo form using uri
    :param uri: api call for wufoo form
    :return: list of entries as json
    
    
    
    
    
create_database(dbname):
    create a database
    :return: Cursor to the database connection
    
    
 
 
 
create_wufootable(conn):
    create wufoo table inside database
    :param conn: connection to the database
    
    
    
    
    
  
 insert_data(conn, i):
    inserts form entries to the wufoo table
    :param conn: connection to the database
    :param i: 1 record of entry
    
    
    
    
    
    
showalldbentries(conn):
    show all the records from the database.
    
    
    
    


populatetable(conn):
    Checking the existence of table and return correct number of user entries.
    :param conn: connection to the database
    :return: list of user entries
 
 
 
 
 
 
 The main function executes based on the function called in the file.
 
 
 
 
 
 
"clock.py"= used to daily schedule job and update the records in every 24 hours.






"queries.py"= file is used to serve querying on the database without any API call.






SERVER TO FETCH ENTRIES FROM DATABASE.

I have used FASTAPI and Uvicorn Server


I have used FastAPI as the framework to build my API, and Uvicorn is the server that I have used.
The Uvicorn server will use the API I build to serve requests.




The ServerAccess.txt file specifies the steps to access the FASTAPI server and retrieve the form entries.


    
    
    
    
    
a brief description of what is missing from the project (if anything)- None from the given







**SPRINT2-DONE**








**Sprint 3: Building a GUI**







MY WUFOO FORM LINK

https://ssahu.wufoo.com/forms/mxys8nv044etu7/








PROJECT DESCRIPTION

I have used pysimpleGUI module of python to build the GUI.
The file cubes_gui.py is the file used to design the layout and window of the GUI.
The GUI retreives data from the server and not from the local database. Hence one needs to run the wufooform.py file to activate the server and then run the cubes_gui.py file to see the Graphical User Interface of the application.





STEPS TO ACCESS THE GUI THROUGH SERVER.



1. Run the file wufooform.py-This file runs the application through FASTAPI.
2. The server gets activated.
3. Run the cubes_gui.py- The GUI for the project is build here.This file shows a visual display of the application and allows user to select the fields and retrieve detailed records. The data is retrieved from the server.






PROJECT REQUIREMENTS
Install Python and import packages json,sqlite3,pysimpleGUI
install packages
requests~=2.28.2
schedule~=1.1.0
APScheduler~=3.10.0
fastapi~=0.90.1
uvicorn~=0.20.0
PySimpleGUI~=4.60.4






TEST CASES




testdatabasehasdata.py-.this file queries the database, and the assert function makes sure the result is none.









testdatafromserver.py->here the request.get function retrieves data from server and displays the response status code.








testguidata.py->this test case checks if the first name, last name and prefix field is populated correctly and also checks if the checkbox is checked.



SPRINT 3 DONE


SPRINT 4 - A GUI with data visualization:

PROJECT DESCRIPTION
This project is use to claim the Graphical Interface Application Project created in Sprint-3
This Project allows user to claim the project by clicking on claim button.
It send an email to the user who claims the project.

STEPS TO ACCESS THE DATA VISUALIZATION THROUGH SERVER.
Step-1-Please run the file wufooform.py file as it activates the uvicorn server
Step-2-Please run the datavisualization.py file, this file displays my GUI project and then allows the user to claim it.

PROJECT REQUIREMENTS
Install Python and import packages json,sqlite3,pysimpleGUI,smtplib
install packages
requests~=2.28.2
schedule~=1.1.0
APScheduler~=3.10.0
fastapi~=0.90.1
uvicorn~=0.20.0
PySimpleGUI~=4.60.4

TEST CASES
testcasesprint4.py-
Test case 1: Create new user
Test case 2: Check existing user
Test case 3: Populate data for existing user
