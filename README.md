# Sqlalchemy-Climate-Analysis-and-Exploration


## Background
After having been working as a data analyst for 2 years, I have decided to have a long holiday vacation in Honolulu, Hawaii. To work out my trip planning, I think I need to do some climate analysis on the area. 

### Source

There is a sqlite database containing Hawaii's climate change in recent years.    


### Data Analysis

1. List the following details of each employee: employee number, last name, first name, sex, and salary.  
 
2. List first name, last name, and hire date for employees who were hired in 1986.  

3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.  

4. List the department of each employee with the following information: employee number, last name, first name, and department name.  
 
5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."  

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.  

https://github.com/LynHJ/Sqlalchemy-Climate-Analysis-and-Exploration/blob/450c53707646bbf2ac81fcbc325bc7352d6ccd37/OutputData/precipitation.png 


### Advanced Data Analysis

1. Create a histogram to visualize the most common salary ranges for employees.  
![alt text](https://github.com/LynHJ/Sqlalchemy-Climate-Analysis-and-Exploration/blob/450c53707646bbf2ac81fcbc325bc7352d6ccd37/OutputData/temperature.png)  
2. Create a bar chart of average salary by title.  
![alt text](https://github.com/LynHJ/Sqlalchemy-Climate-Analysis-and-Exploration/blob/450c53707646bbf2ac81fcbc325bc7352d6ccd37/OutputData/daily-normals.png)  
#### Summary for Advanced Data Analysis

According to the first pictures above,the salary distribution looks normal.When salary increases, the number of who earn that decreases.However, when I use titles to break down the distribution of salary, I found out that those who have high techniche skills or management skills earn less than normal staff. Therefore I assume that this dataset is spurious.


## Content:
Project  
|  
|-&nbsp;EmployeeSQL&emsp;|  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-&nbsp;InputData:&nbsp;|-departments.csv  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-dept_emp.csv  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-dept_manager.csv  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-employees.csv  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-salaries.csv  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-titles.csv  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-OutputData:|-Table Schemata.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis1.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis2.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis3.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis4.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis5.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis6.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis7.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Data Analysis8.sql  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-ERD.png  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-ADA1.png  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-ADA2.png  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-Advanced Analysis.ipynb  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-config.py  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-configtemplate.ipynb  
|-README.md 
|-.gitignore 

## Installation

1.conda env create -n PythonData --file intro_python_requirements_osx.yml python=3.7.7 
2.psycopg2 2.9.3  
3.sqlalchemy  
4.configparse  
5.conda install matplotlib   
6.pgAdmin and Postgres v.14  

## Prerequisites

1.Using config template to create config.ini to run through whole project.  
2.Using pgAdmin to import 6 csv.files to Postgres v.14.  





