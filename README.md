# CGPA-Calculation-Using-Django 
<br>
The CGPA Calculator is a web-based application made with Django ,To help students in calculating their Cumulative Grade Point Average (CGPA) efficiently and securely.
<br>
This project demonstrates how to build a secure CGPA calculator using Django. <br> 
Students can register, log in, and input their Subject Code, Subject Names, CGPA, and Credits.<br>
The project then computes the cumulative GPA and prints the results, also allows to generate in PDF format.

## Features
- User registration and login system for secure access.
- Input fields for Subject Code, Subject Names, CGPA, and credits.
- CGPA calculation and result generation.
- PDF format download functionality for results.

## Requirements
- Python 3.x
- Django 4.x
- ReportLab (for PDF generation)

## Tech Stacks
Django, Python, HTML, CSS

## To run this project
1. You should have Python installed on your computer.It's advised you create a virtual environment to store your projects dependencies separately.<br> You can install virtual environment with
<br>
      py -m venv "name_of_environment"  <!--name_of_environment\Scripts\activate-->
<br>
2. Clone this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project
<br>
3. Open the command prompt (in windows "win+R") in the project directory.Then run the application using the following command
<br>
      py manage.py makemigrations  <!--if you make any change in the files ,makesure to migrate it before running-->
<br>
      py manage.py migrate
<br>
      py manage.py runserver

## Installation

1. Clone the repository:
   ```bash
   https://github.com/yourusername/CGPA-Calculator-using-Django.git
   cd CGPA-Calculator-using-Django

## Project ScreenShots
Login Page



Register as new user 



Adding Subjects



Editing Subjects




Generating Result



Printing PDF

