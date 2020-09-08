# Foodie's Cookbook

### Agenda

This webpage is to assist a user to search for food recipes and/or add his own recipe to the webpage.

### Typographic

The color and fonts have been selected to suit the agenda of the website. Aimed at having colors and font that are pleasant,clear and readable for the users to explore information in our website.

### UX Design

The initial idea of the website and its ux Design has been created in Wireframe. Click here[] to view the desktop and mobile view.

### User Stories

A user who wish to try any new recipe  can search in the webpage or would like to share his own recipe through this website. 

- A visiting user be able to search for new recipes based on type, cuisine, name of the recipe.
- A visiting user be able to see a list of all the recipes on the webpage.
- A visiting user be able to add thier own recipe.
### Features
#### Existing Features
- Header allows users to see the webpage name and also to navigate to different pages of Foodie's Cookbook.
- Navbar allows user to add, search ,list recipes on the webpage.
- Home page  allows user to  search or add recipe.
- Recipe index page lists all the recipes in the webpage.
- In Recipe index page the user is allowed to view, edit and delete recipes.
- Add reipe page allows the user to add a recipe to the database.
- Search page allows user to search recipes based on cuisine, type, title. 
- we have an error page to load on occurance of errors.
#### Features left to Implement
- Add in Login/Signup Feature
- Option to upload Image and store it locally.
- Add and remove items directly.
### Technologies used
#### List of Technologies used
- Flask
- MongoDB
- materializecss
- Javascript
- HTML
- CSS
- Boostrap
- Gitpod
- Github
- Heroku
### Best Practices
- Python code has been validated with Pylint.
    These errors are due to Framework.
    1. app.py:120:13: E1101: Class 'Recipe' has no 'objects' member (no-member).
    2. app.py:140:0: C0103: Argument name "e" doesn't conform to snake_case naming style (invalid-name).
    3. app.py:140:15: W0613: Unused argument 'e' (unused-argument)
    4. app.py:7:0: W0611: Unused InternalServerError imported from werkzeug.exceptions (unused-import)

- Javascript code is checked in https://jshint.com.
- Git comment message clearly says the problem fixed.

### Testing
#### Header Section
##### Test Cases for Desktop view
- Company name should appear on the header.
- Menu options should be displayed horizontally in the header.
- User should be able to navigate to Home Page when clicked the home option in the navigationbar.
- User should be able to navigate to Recipe Index Page when clicked the Recipe Index  option in the navigation bar.
- User should be able to navigate to Add Recipe Page when clicked the Add recipe option in the navigation bar.
- User should be able to navigate to Search Page when clicked the Search recipe option in the navigation bar.
Test Cases for mobile view

- Company name should appear on the header.
- Navbar should be collapse and button with pulldown menu option must appear.
- User should be able to navigate to Home Page when clicked the home option in the navigationbar.
- User should be able to navigate to Recipe Index Page when clicked the Recipe Index  option in the navigation bar.
- User should be able to navigate to Add Recipe Page when clicked the Add recipe option in the navigation bar.
- User should be able to navigate to Search Page when clicked the Search recipe option in the navigation bar.
#### Home Page

Test Cases for Desktop view
- User should be able to view the welcome message.
- User should be able to see image and a write-up about Cooking.
- User should be able to see Add a Recipe card  and Search a recipe card arranged on the same row.
rd arranged one below the other.
- User should goto Search page when Search a recipe button is clicked.
- User should goto add Recipe page when clicked the Add recipe button.
- User should be able to see a menu bar on this page.

Test Cases for Mobile view
- User should be able to view the welcome message.
- User should be able to see image and a write-up about Cooking.
- User should be able to see Add a Recipe card  and Search a recipe card arranged one below the other.
- User should goto Search page when Search a recipe button is clicked.
- User should goto add Recipe page when clicked the Add recipe button.
- User should be able to see a menu bar on this page.

#### Recipe Index Page
Test Cases for Desktop view
- User should be able to view all the recipes list as card.
- User should be able to see each recipe card has the details like title of the recipe,image and descrition.
- User should be able to see View,Edit, Delete option for every recipe listed in the page.
- User should be able to edit the recipe when clicked edit.
- User should be able to view the recipe when view option is clicked.
- User should be able to delete the recipe on clicking delete.
Test Cases for Mobile view
- User should be able to view all the recipes list as card.
- User should be able to see each recipe card has the details like title of the recipe,image and descrition.
- User should be able to see View,Edit, Delete option for every recipe listed in the page.
- User should be able to edit the recipe when clicked edit.
- User should be able to view the recipe when view option is clicked.
- User should be able to delete the recipe on clicking delete.
#### Add Page
Test Cases for Desktop view

- User shouls be able to add the recipe details.
- User should not be able to submit the form leaving any fields empty.

Test Cases for Mobile view

- User shouls be able to add the recipe details.
- User should not be able to submit the form leaving any fields empty.

#### Search Page
Test Cases for Desktop view

 - user cannot leave the search box empty.
 - User can search recipe based on name, cuisine, type.
Test Cases for Mobile view 
 - user cannot leave the search box empty.
 - User can search recipe based on name, cuisine, type.


### Fixed Issues
Fixed issue to store list of fields into database.
Fixed adding input dynamically when add button is clicked.

#### Deployment
The steps to deploy the project locally.

Download the files form the Git respository.
Download option will get the zip folder of the repo.
Extract the zip folder of your choice.
Run the index.HTML in your browser.
Deployment via Gitpod.

In Gitpod,type:python3 -m http.server in the terminal and press enter.
List of open ports will be listed.
Choose port -8000 and cick Open Browser.
Now the project is open in the new tab.
Credits
Media
The images used in the project are obtained from the following:-

Photo by Raphael Andres on Unsplash.
Photo by Anders Jildén on Unsplash.
Code
The google maps api code was obatined from https://developers.google.com/maps/documentation/javascript/examples/place-search-pagination#all.
