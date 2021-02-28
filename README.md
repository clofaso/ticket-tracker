# Ticket Tracker Application

This is a ticket tracking application designed using Django, a Python web framework. Users can create and submit new tickets, as well as view all previously submitted tickets.

### Getting started
To get started, it is recommended to create a virtual environment for any new project.

1. Create a virutal environment on Linux or macOS entering the following in the command line:

```
python3 -m venv envName
```
   *Feel free to replace the **'envName'** with the enviornment name of your choosing*

2. Django can then be installed within the working virtal environment: 

```
pip install -r requirements.txt
```

3. Download the [ticket-tracker](https://github.com/clofaso/ticket-tracker) project files to the virtual environment folder.

### Running Ticket Tracker Web Application
1. To run the server and access the Ticket Tracker web application, enter the following command:

```
python manage.py runserver
```

2. If executed correctly, the following text should appear:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 28, 2021 - 18:18:16
Django version 3.1.7, using settings 'ticket_tracker.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

3. Click on the development server link and a new web page will open in your browser.

4. Explore and create!

### Features
* Python code
* Django web framework
* sqlite3 database
* HTML/CSS

### Citation
[Navigation Top Bar CSS Style](https://github.com/clofaso/ticket-tracker/blob/main/templates/navbar.html): CSS styling for the navigation bar found on [w3schools](https://www.w3schools.com/howto/howto_js_topnav.asp).
