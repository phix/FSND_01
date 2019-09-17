README Section
# Logs Analysis Internal Reporting Tools

## About:
	
	This Reporting tools consists of python codes that talks to Database API With postgresql database using psycopg2 module
	to fetch out reports from psql news query in Git-bash(Command Line) connected to 
	shared file cd /vagrant and live database(newsdata.sql).
	
	"The database contains newspaper articles, as well as the web server log for the site.
	The log has a database row for each time a reader loaded a web page.  
	it will connect to that database, use SQL queries to analyze the log data, and print out the answers to 3 questions."
	1. What are the most popular three articles of all time?
	2. Who are the most popular article authors of all time?
	3. On which days did more than 1% of requests lead to errors?

## Steps to run the software(vagrant and newsdata in postgresql database) and python codes:
	1. Install Git-Bash Unix-Style Terminal for Windows ( https://git-scm.com/downloads )
	2. Install Vagrant Tools to turn on Virtual Machine and Connect to Virtual Box ( https://www.vagrantup.com/downloads.html )
	3. Install VirtualBox; Currently (October 2017), Newer versions do not work with the current release of Vagrant.
	   So the supported version of VirtualBox to install is version 5.1. ( https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 )
	4. Download the VM configuration called FSND-Virtual-Machine for this project ( https://github.com/udacity/fullstack-nanodegree-vm ) 
	5. Download the database file called newsdata.sql and put it in the shared fill directory (/vagrant) 
       **Note: Please Check Udacity's Policy for it ** 
	6. Open Git-Bash cd to FSND-Virtual-Machine Directory and Type Vagrant up; Vagrant SSH
	7. Connect to database newsdata.sql from Step 5; cd into /vagrant directory and use the command psql -d news -f newsdata.sql
	8. Connect to database using psql -d news or psql news	
	9.To quit type \q right after news=> Ex: new=> \q
	10. Go to shared file by cd /vagrant and use the command (python fsnd_log_analysis.py)
