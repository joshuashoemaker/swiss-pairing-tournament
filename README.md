#Swiss Pairing Tournament Test

This project is a test for working with the PSQL database. This is a project 
I completeed for the Udacity Full Stack Nanodegree program.

First run the tournament.SQL file to set up the database, tables, and views.
To do so run this comamnt in your console, assuming you have PSQL installed:

### psql -f tounament.sql

You now have the database, tables and view set up for this project.

Then run the test in your python shell, or in the your operating systems console 
with "python" before this command:

### >>> tournament_test.py

This file runs unit test for the main functions of this project to ensure everything
is structured properly.

The Tournament.py file handles all the inserts and selects from the database 
and returning useful arrays of data to use. It can be used alone in your scripts
if by chance you need to quickly get a Swiss Pairing Tournamnet System.

Perhaps you host game tournaments in your house twice a month with a semi-large
group of friends and coworkers. Maybe you offer prizes to the winner, and the person 
who is almost a winner. Maybe you offer snacks at these tournaments. Regardless, 
this example can get you set up