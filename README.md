# Foodie's Cookbook

### Agenda

This webpage is to assist a user to search for food recipes and/or add his own recipe to the webpage.

### Typographic

The color and fonts have been selected to suit the agenda of the website. Aimed at having colors and font that are pleasant,clear and readable for the users to explore information in our website.

### UX Design

The initial idea of the website and its ux Design has been created in Wireframe. Click here to view the desktop and mobile view.

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
- we have an error page to load during errors.
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
- Python code has been validated with Pylint 
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
#####  Test Cases for mobile view
- Company name should appear on the header.
- Navbar should be collapse and button with pulldown menu option must appear.
- User should be able to navigate to Home Page when clicked the home option in the navigationbar.
- User should be able to navigate to Recipe Index Page when clicked the Recipe Index  option in the navigation bar.
- User should be able to navigate to Add Recipe Page when clicked the Add recipe option in the navigation bar.
- User should be able to navigate to Search Page when clicked the Search recipe option in the navigation bar.
#### Home Page
##### Test Cases for Desktop view
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
- User should be able to see Add  buttons to pick their option.
User should be able to view a google map of Stockholm.
User should be able to view list of cafes in stockholm when he clicks the cafe option button.
User should be able to view list of historic places in stockholm when selected the Culture and Histroy option.
User should be able to View list of shopping places in stockholm when selected the Shopping option.
User should be able to View list of Art Galleries in stockholm when selected the Art Gallery option.
User should be able to view places marked in alphabets on google maps after clicking the radio button.
User should be able to view list of places and map side by side.
User should be able to see list of facts and image scroll of stockholm pictures side by side.
User should be able to see the footer.
Test Cases for Mobile view
User should be able to view the menu bar.
User should be able to see and click radio buttons to pick their option.
User should be able to view a google map of Stockholm.
User should be able to view list of cafes in stockholm when he clicks the cafe option button.
User should be able to view list of historic places in stockholm when selected the Culture and Histroy option.
User should be able to View list of shopping places in stockholm when selected the Shopping option.
User should be able to View list of Art Galleries in stockholm when selected the Art Gallery option.
User should be able to view places marked in alphabets on google maps after clicking the radio button.
User should be able to view list of places and map side by side.
User should be able to see list of facts and image scroll of stockholm pictures side by side.
User should be able to see the footer.
Contact Page
Test Cases for Desktop view
User must be able to view a contact form with Name , Email and Message label and textbox.
Try to submit the empty form and verify that an error message about the required fields (Name,Email) appears
Try to submit the form with an invalid email address and verify that a relevant error message appears.
When user sends the feedback /query the admin must receive the same via email.
User should be able to view header and footer.
Test Cases for Mobile view
User must be able to view a contact form with Name , Email and Message label and textbox.
Try to submit the empty form and verify that an error message about the required fields (Name,Email) appears
Try to submit the form with an invalid email address and verify that a relevant error message appears.
When user sends the feedback /query the admin must receive the same via email.
User should be able to view header and footer.
Fixed Issues
Fixed the google map marker api too customize the marker.
Fixed the list of places adding upon after everyclick without the list clearing itself.
Deployment
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
