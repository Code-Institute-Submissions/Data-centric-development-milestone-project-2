# Foodie's Cookbook

### Agenda

This webpage is to assist a user to search for food recipes and/or add his own recipe to the webpage.

### Typographic

The color and fonts have been selected to suit the agenda of the website. Aimed at having colors and font that are pleasant,clear and readable for the users to explore information in our website.

### UX Design

The initial idea of the website and its ux Design has been created in Wireframe. Click [here](https://github.com/Vanitha-krishnan/Data-centric-development-milestone-project/blob/master/wireframe/Foodiecookbook.png) to view the desktop and mobile view.

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
- HTML5
- CSS3 - CSS3 is used for custome styling the elements.
- JavaScript - JavaScript function is used to overcome the bug in the datepicker.
- JQuery - Jquery is used to initialize the Materialize components.
- Materialize Framework - Materialize front-end framework is used to make website responsive.
- Python - Python is used as the back-end programming language.
- Flask - Python microframework Flask is used to create this project.
- Jinja - Jinja templating language is used with Flask in the HTML code.
- Balsamiq - Balsamiq is used to create wireframes for the project.
- PyMongo - It is a Python distribution that contains tools to work with MongoDB.
- MongoDB - It is a NoSql database that is use to store data at the backend. 
- Git & Github - Used for version control.
- Heroku - It is used as hosting platform to deploy the project.

### Best Practices
- Python code has been validated with Pylint.
    These errors are due to Framework.
    1. app.py:120:13: E1101: Class 'Recipe' has no 'objects' member (no-member).
    2. app.py:140:0: C0103: Argument name "e" doesn't conform to snake_case naming style (invalid-name).
    3. app.py:140:15: W0613: Unused argument 'e' (unused-argument)
    4. app.py:7:0: W0611: Unused InternalServerError imported from werkzeug.exceptions (unused-import)

- Javascript code is checked in https://jshint.com.
- Git comment message clearly says the problem fixed.
- W3C Markup Validation Service for HTML
- W3C Markup Validation Service for CSS


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
- User should not be allowed to submit recipe without atleast one ingredient.
- User should not be allowed to submot recipe without atleast one instruction.

Test Cases for Mobile view

- User shouls be able to add the recipe details.
- User should not be able to submit the form leaving any fields empty.
- User should not be allowed to submit recipe without atleast one ingredient.
- User should not be allowed to submot recipe without atleast one instruction.

#### Search Page

Test Cases for Desktop view

 - user cannot leave the search box empty.
 - User can search recipe based on name, cuisine, type.
 - All the recipes has to be displayed on click of Reset button.

Test Cases for Mobile view 
 - user cannot leave the search box empty.
 - User can search recipe based on name, cuisine, type.
 - All the recipes has to be displayed on click of Reset button.

### Fixed Issues
Fixed issue to store list of fields into database.
Fixed adding input dynamically when add button is clicked.

#### Deployment
Deployment in Github
1. Go to Data-centric-development-milestone-project Github Repository
2. Click on Code beside Gitpod.
3. A drop down menu open then click on Download Zip
4. Unzip the downloaded zip file.
6. Create a database in MongoDB called cookbook.
7. Create a collection with name "recipe"
8. Open app.py file and install requirements.txt by running comman pip3 install -r requirements.txt.
9. Create env.py file and add MONGO_URI and SECRET_KEY.
10. Now run the app.py by running code python3 app.py

 Deployment in Heroku

  To deploy the website in Heroku, follow the instructions given below.

 1. Login to Heroko account.
 2. Created the app in Heroku.
 3. Create App by providing Name and Region.
 4. Also create requirement.txt in terminal window using  pip3 freeze --local > requirements.txt.
 5. Create Procfile
 6. Add,commit and push those files in github.
 7. Go to Settings at the top. Then click on Reveal Config Vars.
 8.	In Config Vars add IP with value 0.0.0.0 then add PORT as 5000 then add SECRET_KEY then add MONGO_URI and then add MONGO_DBNAME which is the name of database.
 9. App is deployed.
 10. In domians in settings has the link to your app.
 11. Click the link to see your webpage launched.
 

#### Credits

The recipes for this webpage was obtained from the folloing pages.

- https://www.homecookingadventure.com/recipes/chocolate-rose-cake
- https://naturallynidhi.com/tomato-basil-focaccia/
- https://www.delscookingtwist.com/easy-fluffy-american-pancakes/
- https://food.ndtv.com/recipe-crunchy-iceberg-dumpling-914651
- https://www.allrecipes.com/recipe/256398/spongy-japanese-cheesecake/

The images and the recipes are used for educational purpose only.
