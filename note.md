## HTML file:

    ecommerce/templates/html

## CSS file + picture + File html 

    static/assests : css
        1. For navigation bar - other files inherit from this file: nav.html - nav.css
        2. For first homepage: home.html - page.css 
        3. For information company: about.html - No file css yet. 
        4. register and signin: 
                + register.html - register.css
                + signin.html - signin.css
        5. For display the product. This page is for after login => homeMain.html - no css yet
        6. To display a unque product. => product.html - no css yet
        
    static/images : picture
    media: for the picture of products

## back-end

    models.py : database elements
    urls.py: path/ link
    views : connect to html, functions
    forms : form input

## To run server:

    python manage.py runserver

## To manage database:

   [Press here !](http://127.0.0.1:8000/admin/)
   
   - Account: admin11
   - password: @team0011
## To add admin account:
    Way 1: python3 manage.py createsuperuser
    Way 2: access to account above => users => add
## Update database: 
    python3 manage.py makemigrations
    python3 manage.py migrate
## Check the sqlite3 
    python3 manage.py shell
``` Recommendation: Please note here about your code's knowledge or  at least comment on what your functions represent. That will help teammates to understand better and catchup easily. ```