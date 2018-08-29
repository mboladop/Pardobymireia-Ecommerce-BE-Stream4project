[![Build Status](https://travis-ci.org/mboladop/Pardobymireia-Ecommerce-BE-Stream4project.svg)](https://travis-ci.org/mboladop/Pardobymireia-Ecommerce-BE-Stream4project)


# Pardo by Mireia ecommerce Website
![Desktop Demo](https://raw.githubusercontent.com/mboladop/Pardobymireia-Ecommerce-BE-Stream4project/master/README_linked_files/stream4desktop.gif "Desktop Demo")
 
## Overview
 
### What is this website for?
 
This is an ecommerce website for people to shop all Pardo by Mireia´s latest products and keep them informed of the brands whereabouts.
 
### How does it work
 
This website uses **Python3** as primary language and **Django** as the framework to route viewers through the site. The site is styled with **Bootstrap**, **css3**,  **Font Awesome** and **Google Fonts**. The chat data is stored in a **sql DB** in local and a **Postgres DB** in production. It also uses **Amazon Web Services (AWS)** to store all the static for production and **Stripe** as payment platform.

## Instagram API 

This part of the project comes from a specific need of the client. The idea is basically to simplify for the customer the search of the most wanted products which are normally the ones promoted through the social media profiles of the brand.
The shop instagram section created mimicks the brands real IG profile and conects every item features in the instagram profile to the product profile in the DB (if it exists/is still available).

The conection to the IG API is done in the views.py of the shopinstagram app. This was the hardest part cause getting the API token isnt as easy as the documentation found explains. They also advice the posibility of the token being disabled anytime given the fact the IG API is experiencing major changes. Once the conection is made the data was [jsonified](http://jsonparseronline.com/) and the data needed was the photo url. Once this was clear product.models.py was modified to include a new text field where the link provided by IG as a url needed to be pasted if the product existed in the database.

If the product has been featured in IG when hover on the photo there is a button that links to the product profile and can be easily added to the cart.


## Features
 
### Existing Features
- Simple and clean layout.
- Easy and intuitive UX display.
- Clean Landing.
- Contact forms.
- Stripe as payment method.
- Shop Instagram section were the website connects to IG API and mimicks the brands profile linking the pictures of the available products with their profiles.
- Easy hover add to cart button.
- Login/out, Register and password reset available.
- Blog and New/in sections.

### Features Left to Implement
- New in section responsive.
- Email send with email.js or own smtp.(There´s a virtual one that displays in the terminal)
- EN/ES version.
- Sizes for anillos category 1-6.
- Add two more images to the Landing page.(Client´s request).
- Update a way to do the shop instagram section ensuring the token or finding another method.


## Technologies Used

- **HTML5**, **CSS3**,  and very lightly **Javascript**
  - Base languages used to create website.
- **Django 2** as the framework for **Python3**.
- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give the project a simple, responsive layout.
- [Google Fonts](http://googlefonts.com/)
    - We use **Google Fonts** to give our project the fonts.
- [Postgres DB](https://www.postgresql.org/)
    - We use **Postgres DB** to store the static in production.
- [sql DB](https://www.mysql.com/)
    - We use **sql DB** to store the static in local.
- [Stripe](https://stripe.com)
    - We use **Stripe** as payment platform.
- [IG API](https://www.instagram.com/developer/)
    - We use **IG API** as a way to simplify purchases for the client and better acces to specific products of the brand pictured through the social media platform.


## Manual Testing
- All code/links/forms used on the site have been tested to ensure everything is working as expected.
- Site viewed and tested in the following browsers:
  - Google Chrome
  - Safari
- Site viewed and tested in the following devices:
  - Iphone 7plus
  - Iphone x 
  - Ipad
  - Macbook 13" and 15"
  - Samsung Galaxy

## Automated Testing

All automated testing (81% coverage) was done using Travis-CI. There is automated testing done for each app. 
To use Coverage:

$ pip3 install coverage 
$ coverage run manage.py test (app name)
$ coverage html 
**(creates an htmlcov folder I ignored)**
$ .gitignore
$ python3 manage.py test

This permits viewing the percentage of cover your tests run:

$ coverage run manage.py test
$ coverage report


# How the project looks and works on different browsers and screen sizes:

### Front-end Design
To design a quality front-end design of the ecommerce I decided the best way of aproaching it was to develop the front end in a different repository to the one used for the back-end. Once the design met the expectations, I adapted it to the back-end already developed to meet the clients needs. 
![Static front-end repository of the ecommerce](https://mboladop.github.io/Pardobymireia-Ecommerce-Static-Stream4project/)
This way of planning the project helped me to focus high styling goals, these weren´t limited by any crash that trying to develop front-end and back-end toguether might´ve caused. In general I found this solution extremely effective and learned how to connect a finished front-end with a finished back-end, to overcome bugs that might occur during the process and know how to fix them.

![Responsive Demo](https://raw.githubusercontent.com/mboladop/Pardobymireia-Ecommerce-BE-Stream4project/master/README_linked_files/stream4responsive.gif "Responsive Demo")
 
# BUGS
To test it in different devices i started using the console toggle device toolbar, when I fixed all the versions for the different tablets and mobile screens I opened the website  from my Iphone and realised the display was not looking as it should.
To fix this I created a specific and new mobile version. For this purpose i downloaded Xcode simulator and served the website via [npm package serve](https://www.npmjs.com/package/serve) to be able to access it instantly and remotely through my own phone.


## Deployment (Heroku)

1. Create workspace in Visual Studio Code.
2. Associate it with GitHub repository.
3. Open a new app in Heroku (Europe) choose GitHub as deployment method and choose the repository of your project. This will enable yopur app to be updated with each push you make to Github if you wish.
4. The first time make sure you deploy it manually and then enable automatic deployments choosing master as the branch.
5. On your project workspace:
	$ pip3 freeze --local > requirements.txt
	$ pip3 install gunicorn
  - Check gunicorn is now in requirements.txt by repeating : 
  $ pip3 freeze --local > requirements.txt 
  $ touch Procfile         
  - Open Procfile and paste:               
    web: gunicorn chat:app
  $ git push 
  - In this case I used a **Postgres DB**, **Stripe** and **Amazon Web Services (AWS)**. I was using a bashrc file to store the **DATABASE_URL**, **AWS KEYS**, **SECRET KEYS**, **STRIPE PUBLISHABLE/SECRET KEY** and **IG API ACCESS TOKEN/ USER ID** make sure to include these in the Heroku settings Config vars.


## Contributing

### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command.
2. After you've done that you'll need to make sure that you have **npm** installed. Link [npm package serve](https://www.npmjs.com/package/serve)
3. You must include in bash with **export** the configuration variables above mentioned. Also including: **DEBUG** and the **DJANGO_SETTINGS_MODULE**.
4. The project will now run locally.
5. Make changes to the code and if you think it belongs in here then just submit a pull request.

## Credits

### Media
- The animated Gifs of the different projects from the [Giphy Capture App](https://giphy.com/apps/giphycapture)
- The photos used in this site were obtained from the clients database. 
- The form design for the user login was an adapted version of the one found in [Colorlib](https://colorlib.com)

### Information
- The information used to create this site (materials, sizes and the rest of the pdfs) were provided by the client **Pardo by Mireia Pardo**.

### Inspiration and tutorials
- [How to Create a Password Reset View By Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html)

- [Python Client for Instagram API](http://instagram.com/developers https://github.com/facebookarchive/python-instagram)

- The aesthetical inspiration used to create this site was from a number of sources:
     - Different jewelry ecommerce sites.You can download the Wireframe:[HERE](https://raw.githubusercontent.com/mboladop/Pardobymireia-Ecommerce-BE-Stream4project/master/README_linked_files/wireframe.pdf)
     

## Project Live:
[Link to project](https://mboladop-mireia-ecommerce.herokuapp.com/)


