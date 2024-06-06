<h1 align="center"> FootBrazil - portal of the Brazilian national team</h1>

![image](/static/images/readme-img/background-home-page.png)

### Live Site

- Go to live site - [FootBrazil](https://footbrazil-a7d96ef49755.herokuapp.com/)

### Repository

- Go to the repository for this project, [Repository-Footbrazil](https://github.com/Askeran17/footbrazil.git)

---

## [Contents](#contents)

- [Overview](#overview)
- [Adaptability](#adaptability)
- [User Experience (UX)](#user-experience-ux)
  - [Project goal](#project-goal)
  - [User Stories](#user-stories)
  - [Agile Methodology](#agile-methodology)
  - [Design](#design)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
- [Features](#features)
    - [Existing Features](#existing-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Deploy on Heroku](#deploy-on-heroku)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## Overview

This site is dedicated to the history of Brazilian football, namely the participation of the Brazilian national team in the World Cup. On this site you will find statistics on the performance of the Brazilian national team at the World Championships, a brief historical excursion and review articles on the famous periods of participation of the Brazilian national team at the World Championships where in each post there will be an article, as well as a video review and under these posts each participant will be able to leave a comment and share impressions and memories.

FootBrazil - was developed using HTML, CSS, Javascript and Python (Django).

## Adaptability on a variety of screen sizes

![The FootBrazil on a variety of screen sizes](/static/images/readme-img/adaptability-size.png)

## User Experience

### Project goal

The purpose of the site is to provide, with the help of web development, visitors the opportunity to easily immerse themselves in the atmosphere of the Brazilian national team and its participation in the World Cup.

### User Stories


### Agile methodology

This project was developed using the agile methodology. Necessary goals and priorities were well defined throughout the project. In addition, labels were used to define the priority of each user story.

Visitors can read posts and view video but not to add a comment under this. Registred users can add a comment under posts. Administrator of site can adding, updating & deleting comments. When user stories were completed, they were moved from the To Do via Progress to Done list.

Here is link to Agile [User Stories](https://github.com/users/Askeran17/projects/5/views/1).

### Design

- The design of the website should be combined with the theme, and since the theme of the site is the Brazilian national football team, the design of the website is focused on the combination of the colors of the Brazilian national team.

#### Colours

- The color scheme predominantly consists of a variety of greys, greens, whites and blues. The use of gray and dark white creates a background tone, while the green is refreshing and correlates with one of the colors of the Brazilian flag, which matches the theme of the website. The blue color brightens up dark colors and, like green, is part of the Brazilian flag. The black color clearly indicates the bottom panel of the site.

![image](/static/images/readme-img/colours-palette.jpg)

#### Fonts

-  In order for the site to blend beautifully with the text, two text styles were used:

<br>

<strong>"Jersey 10"</strong> - was used for the main page as a welcome message, which goes well with the main image of the site. 

Here is an example:

![image](/static/images/readme-img/jersey-10-font.png)

<br>
<strong>"Exo"</strong> - was used as the main style of page texts.

<br>
Here is an example:

![image](/static/images/readme-img/exo-font.png)

<strong>"Crimson Text"</strong> - this style took just in case, but I didn’t use it


### Wireframes
I used program "Balsamiq Wireframes" to draw a page layout.

![image](/static/)

### Database Schema
The project uses the relational database PostgreSQL to store the data.


## Features

### Existing Features

## Technologies Used

In the beginning I did all the work in Codeanywhere, but after I switched to GitPod platform.

### Languages Used

HTML, CSS, JavaScript, Python, Django

### Frameworks, Libraries & Programs Used

* [Django](https://pypi.org/project/Django/4.2.11/) - To start project in Python.

* [Bootstrap](https://getbootstrap.com/) - To create the front-end design.

* [GitHub](https://github.com/) - To save and store the files for the website.

* [GitPod](https://gitpod.io/) - To use as IDE to commit and push the project to GitHub.

* [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

* [Google Developer Tools](https://developers.google.com/web/tools) - To troubleshoot and test features, solve issues with responsiveness and styling.

* [IloveImg](https://www.iloveimg.com/) - To resize images.

* [Convertio](https://convertio.co/) - To convert images to webp format.

* [Favicon.io](https://favicon.io/) - To create favicon.

* [Balsamiq](https://balsamiq.com/) - Used to create wireframes.

* [Am I Responsive?](http://ami.responsivedesign.is/) - To show the website image on a range of devices.

* [Emojipedia](https://emojipedia.org/) - Emoji for history timeline.


## Testing

Throughout the development of the site, I used Google's developer tools to identify and fix any problems along the way.

If something didn't work correctly, I also used Google's developer tools to tweak and fix the problem.

I've thoroughly tested each page using Google Chrome's developer tools to ensure each page is responsive on a variety of screen sizes and devices.

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

The site showed good scores.

Home page
![Home](/static/images/readme-img/desktop-index.png)

Full Post page
![Full post](/static/images/readme-img/desktop-full-post.png)

History page
![History](/static/images/readme-img/desktop-history.png)

About page
![About](/static/images/readme-img/desktop-about.png)

### Mobile Results

The site showed good scores.

Home page
![Home](/static/images/readme-img/mobile-index.png)

Full Post page
![Full post](/static/images/readme-img/mobile-full-post.png)

History page
![History](/static/images/readme-img/mobile-history.png)

About page
![About](/static/images/readme-img/mobile-about.png)

### Manuel Testing

I conducted manual testing to ensure the effectiveness and usability of the FootBrazil website.

#### Homepage

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view home page | Access the main page of the website | Being able to open and browse without errors | PASS |
| Visitor can click on all button in homepage | When hover over the button, the button darkens a little| Buttons works without errors | PASS |
| Homepage displays posts | Navigation from background image to posts | Posts shows without errors | PASS |

#### Detailed post page

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view detailed post page | Access to the post page after clicked on button "click to read" from homepage | Being able read text and watch on video without errors | PASS |
| Registered user can leave a comment under post | Log in and leave a comment | Leave a comment without errors | PASS |
| Comment appears after approval | Leave a comment and wait until admin approve it | Comment appears after approval without errors | PASS |

#### Add post page

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Admin can add post from website itself | Access to the add post page after clicked on button "Add post" from navbar | Being able to fill out the fields, send it and post will be added on homepage directly | PASS |
| Image uploading from add post page | Opportunity to have a field to upload image to post | Image appears without errors | PASS |
| Sponsor appears | Opportunity to choose sponsor for post | Сheck the box below the post and after post creating it will appear sponsors name without errors | PASS |

#### History page

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view history page | Access to the history page after clicked on button "History" from navbar | Being able read text without errors | PASS |

#### About page

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view about page | Access to the about page after clicked on button "About" from navbar | Being able read text without errors | PASS |

#### Registration 

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| User signup page | Click on button "Register" from navbar | Visitor is directed to the signup page | PASS |
| Fill in the registration form with valid and unique user information | Click on button "Sign up" | Success full registration | PASS |

#### Footer

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Social media link opens with new tab | Click on link "Facebook, Twitter, Instagram or Youtube" from footer | Visitor is directed to the new window for selected socialmedia | PASS |

#### Navbar

| Testing  | Steps | Expected Outcome | Grade |  
| - | - | - | - |
| Navbars link testing | Each link will be working correctly | The user can open any link to view the web page | PASS |

#### Admin

| Testing  | Steps | Expected Outcome | Grade |  
| - | - | - | - |
| Superusers features | Superuser will be able to create, delete and update | Superuser can create, delete and update content | PASS |


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/)

- JAVASCRIPT
  - No errors were returned when passing through the official [JSHint validator](https://jshint.com/)

- PYTHON
  - No errors were returned when passing through the PEP8 Validator 

- Admin.py
  ![admin.py](/static/images/readme-img/admin-py.png)

- Models.py
  ![models.py](/static/images/readme-img/models-py.png)

- Views.py
  ![views.py](/static/images/readme-img/views-py.png)

- Urls.py
  ![urls.py](/static/images/readme-img/urls-py.png)

- Forms.py
  ![forms.py](/static/images/readme-img/forms-py.png)
  

### Unfixed Bugs

Here is unfixed bugs.

## Deployment

### Local Development

Deployed using Heroku.

1. Log in/sign up to Heroku.
2. Go to your Heroku App and click on "Deploy".
3. At section "Deployment method", click "GitHub" and connect your account with Heroku.
4. When you're connected, search for the project you wanna connect the app to and click on it.
5. Click "Deploy Branch".
6. Your app will now be deployed to GitHub and when it's done you can click "Open App".

#### How to Fork
Fork the repository:<br>
1. Log in/sign up to GitHub.
2. Go to the repository for this project [FootBrazil](https://github.com/Askeran17/footbrazil).
3. Click the 'Fork' button in the top right corner.

#### How to Clone
Clone the repository:<br>
1. Log in/sign up to GitHub.
2. Go to the repository for this project [Footbrazil](https://github.com/Askeran17/footbrazil).
3. Click the code button, select which one you want to clone with (HTTPS, SSH or GitHub CLI) and copy the link shown.
4. Open the terminal in a code editor and change the current working directory to a location of your choice to use for the cloned directory.
5. Type 'git clone' in the terminal, paste the link that you copied in step 3 and then press enter.


## Credits

I was inspired by the "I Think Therefore I Blog" and "Flask Framework" Rosie project at the Code Institute. So I partially took the code from each project.

### Content 

- All content for the site was written by myself.

- The icons was taken from [Font Awesome](https://fontawesome.com/)

### Media

- The images in site I took from open source, i.e. google.