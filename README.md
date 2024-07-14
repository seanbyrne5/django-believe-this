# **Project Portfolio 4**

![]()

You can view the live site here - <a href="" target="_blank"></a>

# Objective



[Back to top](<#contents>)

# User Experience (UX)

## Site Aims


## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board which can be seen here -  <a href="" target="_blank"></a>

Through the use of the Kanban board in the projects view in Github, the project was divived into a few different sections:
* Backlog
* Current Iteration
* In Progress
* Done

![Kanban board github]()

Github issues were used to create User Stories and any other Fixes or Updates for the project. This was where the project user was assigned, labels were added to provide clarity, and the story was added to the appropriate Iteration and the project. Each User Story, Fix or Update had a clear title, acceptance criteria and smaller tasks (if appropriate). 

Milestones were used to create Iterations. There were 3 Iterations each dated appropriately. User Stories were completed based on the current Iteration that was in progress. Each Iteration was completed on time.

Development branches were used to complete User Stories. This offered a greater level of control in developing the various aspects of the website. Certain User Stories could also be grouped together and worked on in one development branch. Once the User Stories were completed within the branch and the deveoplment branch was up to date with code pushed, a pull request was created. Using the **Closes #User-Story-number** keyword, the various in progress User Story issues that were being worked on would automatically be closed when the pull request was merged with the main branch. The development branch would then be deleted and a new one created with a new set of user story/ies to be worked on.

The Github issues were not just used to record User Stories but also used to **FIX**, **UPDATE** and record **DOCUMENTATION** updates as well, with the use of these words in the issue title to keep track of work done, needing to be done.

### User Stories

**Iteration 1**
* As a **user**  I can **easily see the purpose of this website on the home page** so that **I can easily navigate it**
* As a **user**  I can **view a list of book genres** so that **so that I can see a list of book reviews in a genre I am currently in**
* As a **user**  I can **view a paginated list of books** so that **I can view book reviews easily**
* As a **user**  I can **save books** so that **that I can have a list of books I want to read in the future**
* As a **user**  I can **create a review for a book** so that **so that I can let other's know what I thought of the book**
* As a **site admin**  I can **add a book listing** so that **users can review a book that isn't already on the website**
* As a **user**  I can **see a list of books already reviewed by all users** so that **I can find a new book to read**
* As a **user**  I can **register an account** so that **so that I can review books I have read and save books I want to read**
* As a **user**  I can **choose the category for a book I upload** so that **the book is easily searchable**
* As a **site admin**  I can **approve or decline reviews and book listings made** so that **I can filter out ingenuine reviews or duplicate book records**

**Iteration 2**
* As a **user**  I can **fill out a contact form** so that **so that I can easily contact**
* As a **user**  I can **update and delete reviews I have already made** so that **I can have control over content I have posted**
* As a **user**  I can **save books** so that **I can easily see books of interest to me**
* As a **user**  I can **see my book reviews, username and liked books on a profile page** so that **I can easily keep track of my activity on the site**
* As a **user**  I can **see reviews I have made** so that **I can edit, update or delete my reviews**
* As a **user**  I can **search the website for books** so that **so I can easily find book lisitings**
* As a **user**  I can **add book listings** so that **review a book that isn't already in the database**

**Iteration 3**
* As a **site admin**  I can **access book listings and reviews to be approved** so that **I can approve or not approve and delete user uploads**
* As a **user**  I can **see if I navigate to a wrong page on the website** so that **navigate easily back via the navbar**
* As a **user**  I can **see if I navigate to a wrong page on the website** so that **navigate easily back via the navbar**
* As a **site admin**  I can **access book listings and reviews to be approved** so that **I can approve or not approve and delete user uploads**


## NewmSection



## Database Schema

![Database Schema]()

## Site Structure


## Design Choices

### Color Scheme

![]()

### Typography

[Back to top](<#contents>)

# Features

## Navigation


    ![Navbar Admin Logged In]()

![Username]()

## Home Screen



 ![Homepage Desktop]()

 ![Homepage Mobile]()

 

  ![Homepage Logged In]()


 ### Genre Section

 ![Genre Desktop Page]()



 ![Genre Mobile Page]()

## Log In Page

  ![Log In page desktop]()

![Log In page mobile]()

## Sign Up Page

![Sign Up page desktop]()


![Sign Up page mobile]()

## Log Out Page

![Log out page desktop]()


![Log out page mobile]()

## Bookshelf Page

![Bookshelf page desktop - user not logged in]()

![Bookshelf page mobile - user logged in]()

## Book Page

![user logged in]()

![user logged out]()

![user logged in]()

### Create a Review

![Log in to review]()


![Review added alert]()

![Review form - user logged in]()

### New Section


![]()


![]()

## 

![]()

![]()

### User Reviews
![]()

![]()

![]()



## Contact

![]()

![]()


![]()

![]()


![]()


![]()

![]()

* The page is fully responsive


## New Section


![]()

![]()


### New section

![]()



![]()


![]()

### New section

![]()


![]()

## Star Ratings


![]()
![]()

*
![ Star Rating]()
![ Star Rating ]()

## 404 Page

![404 Desktop Page](docs/images/404-desktop.png)

* A custom 404 page was created for any pages not found.
* This custom page allows the user to navigate back to website via the navbar if they click/type a url which causes a 404 error.
* The page has text and a cute image informing the user of their mistake.
* The page is fully responsive.

![404 Mobile Page]()

## 403 Page

![403 Desktop Page]()

* A custom 403 page was created for user's trying to access pages they do not have access to.
* This custom page allows the user to navigate back to website via the navbar if they click/type a url which causes a 403 error.
* The page has text and a cute image informing the user of their mistake.
* The page is fully responsive.

![]()


[Back to top](<#contents>)

# Future Features

## Book Genre

Currently the book genres play a small role on the website. The genre's themselves are already preset and the user just has to select the genre to go with the book. In the future the genre section would be a section all by itself. It would utilise a tag system, whereby books could have and be search for by multiple genres.

## Social Media Login

For ease of use, user's could use their social media credentials to log in, rather than creating another password to remember.

## Admin Specific Buttons


## More Detailed User Profile Page




## Better Pagination


[Back to top](<#contents>)

# Technologies Used

* HTML - Used to structure all the templates on the site
* CSS - to provide extra styling to the site
* Python - To provide functionality to the site. Packages used in the project can be found in requirements.txt
* Django - Python framework used in the project
* Heroku - Used to deploy the site publicly
* Heroku PostgreSQL - Used for the database during development and deployment
* Javascript - Minimum javascript was used, to initialise and set some settings for packages such as EmailJS and Owl Carousel
* Bootstrap 5.2.0 -  used for providing layouts and styling the html in the templates
* Font Awesome - All icons throughout the page
* Owl Carousel - Used to create a carousel on the home pages and genre pages of the site
* Adobe Illustrator - Used to edit any vectors or svgs for the project
* Figma - Used to create wireframes for the progect
* Diagram.net - Used to create Diagrams for the project
* Cloudinary - Used to host Static files for the site
* VSCode - Used to create, edit and compile the code for the program
* EmailJS - Used to enable the contact form functionality
* Django-star-ratings - Used to enable star ratings functionality on the book listings


[Back to top](<#contents>)

# Testing

I have included testing details in a separate document called [TESTING.md](TESTING.md)

[Back to top](<#contents>)

# Deployment

## Deployment to Heroku

### 1. Creating the Django Project
* If development if being done locally: Activate your virtual environment
* To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
* Install Django and gunicorn: `pip install django gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 library: `pip install dj_database_url psycopg2`
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
* Create file for requirements: `pip freeze --local > requirements.txt`
* Create project:`django-admin startproject project_name .`
* Create app: `python manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: `python manage.py migrate`
* Test server works locally: `python manage.py runserver`

### 2. Create your Heroku app
* Navigate to the Heroku website
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app
* In the Heroku dashboard click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory
* Add env.py to the .gitignore file
* In env.py import the os library
* In env.py add `os.environ["DATABASE_URL"]` = "Paste in the text link copied above from Heroku DATABASE_URL"
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`
* In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 4. Setting up settings.py

* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku  add cloudinary url to 'config vars'
* In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (note: this must be removed for final deployment)
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: ```ALLOWED_HOSTS =
['rhi-book-nook.herokuapp.com', 'localhost']```
*Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Make an initial commit and push the code to the GitHub Repository.
    ```git add .```
    ```git commit -m "Initial deployment"```
    ```git push```

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku
* In the 'Deployment method' section select 'Github' and click the 'connect to Github' button to confirm.
* In the 'search' box enter the Github repository name for the project
* Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

### 6. Final Deployment
In the IDE: 
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. Changes can be made on this copy without affecting the original repository.

1. Log in to GitHub and locate the repository in question.
2. Locate the Fork button which can be found in the top corner, right-hand side of the page, inline with the repository name.
3. Click this button to create a copy of the original repository in your GitHub Account.

## To clone the repository on GitHub

1. Click on the code button which is underneath the main tab and repository name to the right.
2. In the 'Clone with HTTPS' section, click on the clipboard icon to copy the URL.
3. Open Git Bash in your IDE of choice.
4. Change the current working directory to where you want the cloned directory to be made.
5. Type git clone, and then paste the URL copied from GitHub.
6. Press enter and the clone of your repository will be created.

[Back to top](<#contents>)

# Credits

[Back to top](<#contents>)

# Acknowledgements


[Back to top](<#contents>)