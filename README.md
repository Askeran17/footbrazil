<h1 align="center"> FootBrazil - portal of the Brazilian national team</h1>

![image](/static/images/readme-img/background-home-page.png)

### Live Site

- Go to live site - [FootBrazil](https://footbrazil-a7d96ef49755.herokuapp.com/)

### Repository

- Go to the repository for this project - [Repository-Footbrazil](https://github.com/Askeran17/footbrazil.git)

---

## [Contents](#contents)

- [Overview](#overview)
- [Adaptability](#adaptability)
- [User Experience (UX)](#user-experience-ux)
  - [Project Goal](#project-goal)
  - [User Stories](#user-stories)
  - [Agile](#agile)
  - [Design](#design)
    - [Wireframes](#wireframes)
    - [Database](#database)
- [Features](#features)
    - [Existing Features](#existing-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## Overview

This site is dedicated to the history of Brazilian football, namely the participation of the Brazilian national team in the World Cup. On this site you will find statistics on the performance of the Brazilian national team at the World Championships, a brief historical excursion and review articles on the famous periods of participation of the Brazilian national team at the World Championships where in each post there will be an article, as well as a video review and under these posts each participant will be able to leave a comment and share impressions and memories.

Only 6 posts were selected for the site, 4 of which are intended to tell the user about the best performances of the Brazilian national team at the World Cup, namely the 1970, 1982, 1994, 2002 World Cups, as well as 2 more posts dedicated to the two recently held World Cups 2014 and 2022 where the user will be able to compare the past generation of the national team with the current one.

## Adaptability on a variety of screen sizes

![The FootBrazil on a variety of screen sizes](/static/images/readme-img/adaptability-size.png)

## User Experience

### Project Goal

The purpose of the site is to provide, with the help of web development, visitors the opportunity to easily immerse themselves in the atmosphere of the Brazilian national team and its participation in the World Cup.

### User Stories

### Agile

The project used a Agile methodology that tracked the process of creating the project. An issue was created for each user story.

Visitors can read posts and view video in posts but not to add a comment under this. Registred users can add a comment under posts. Administrator of site can adding, updating & deleting comments. A project Kanban board was used to track progress, with user stories moved between 'ToDo', 'In Progress' and 'Done' columns as appropriate.

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

Home page
<br>

![image](/static/images/readme-img/wireframe-home.png)

Detailed post page
<br>

![image](/static/images/readme-img/wireframe-post-detailed.png)


History page
<br>

![image](/static/images/readme-img/wireframe-history.png)

About page
<br> 

![image](/static/images/readme-img/wireframe-about.png)

### Database
The project uses the relational database PostgreSQL to store the data. I used PostgreSQL because it is considered one of the recommended databases on the Heroku platform.

**Post model:**

The model consists of the following parts:

- [x] **title**: models.CharField(max_length=300, unique=True) - Indicates the title of the post with 300 characters length
- [x] **slug**: models.SlugField(max_length=300, unique=True) - automatically creates a 300-character address bar path based on the post title
- [x] **featured_image**: CloudinaryField('image', default='', blank=True) - load images to post from Cloudinary
- [x] **description**: models.TextField(default='') - detailed description of the post
- [x] **summary**: models.TextField(blank=True) - short description of the post
- [x] **sponsor**: models.CharField(default='Embratel', max_length=100) - by default, posts are set to sponsor Embratel
- [x] **has_sponsor**: models.BooleanField(default=False) - the ability to indicate or not indicate a sponsor in a post
- [x] **status**: models.IntegerField(choices=STATUS, default=0) - indicates the status of the post, published or in draft
- [x] **author**: models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    ) - indicates who the author of the post is, and I set up the site so that only the admin can add posts
- [x] **date**: models.DateField('Publication date', default=timezone.now) - post publication date

**Comment model:**

The model consists of the following parts:

- [x] **post**: models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments") - indicates that a comment will be attached to the post
- [x] **author**: models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter") - indicates who is the author of the comment on the post
- [x] **text_comments**: models.TextField('Texts field', max_length=2000) - field for writing a comment with a maximum length of 2000 characters
- [x] **approved**: models.BooleanField(default=False) - a comment must first be approved by an admin before it can be published, all registered users can leave comments
- [x] **created_on**: models.DateTimeField(auto_now_add=True) - comment publication date

## Features

### Existing Features

__Header__

- The header has an adaptive navigation bar on the right. There are five links there for unregistered users: home, history, about, register and login. The visitor can easily navigate through these links thanks to the responsive bar. Also, in the mobile or medium screen extension version, there will be a “hamburger” icon on the right side of the adaptive panel, which means that the same links are hidden behind it. This is very convenient and allows you to take up less page space.

![Navbar Desktop](/static/images/readme-img/nav-menu-desktop-visitor.png)
![Navbar Mobile](/static/images/readme-img/nav-menu-mobile-visitor.png)

- For a registered user, the navbar will look like this:

![Navbar Reg.User](/static/images/readme-img/nav-menu-reg-user.png)

- For admin, the navbar will look like this:

![Navbar Superuser](/static/images/readme-img/nav-menu-superuser.png)

- On the left side of navbar there is a logo that can be clicked and it will return the visitor to the main page.

- When user is logged in, it appears message on the header:

![User logged in](/static/images/readme-img/message-sign-in.png)

- When user is logged in, it appears message on the header:

![User logged out](/static/images/readme-img/message-sign-out.png)

__Main content__

- On the first page the visitor can see a large image of brazilian football stars: Ronaldinho, Neymar, Ronaldo, Romario and Pele and welcome text with button "Go to posts".

<br>

![Go To Posts Button](/static/images/readme-img/go-to-posts-button.png)

![Large image Brazilian Football Stars](/static/images/readme-img/large-image-brazil-stars.png)

- Under the image user will find a short description by brazilian football national team. 

- Under short description user will find six posts of written about participian by brazilian national team at the World Cups on 1970, 1982, 1994, 2002, 2014 and 2022. These world cups was choosen to show for visitors how succesfully and unsuccesfully was brazilian team in those cups. User can go these post either to click on button "Go to posts" placed on large image in header or just by scrolling down.

Due to the fact that only 6 posts were selected on the site, for this reason I did not add pagination code to the template

![Six Posts](/static/images/readme-img/six-posts.png)

__Footer__

- In the footer I have placed a link to Facebook, Instagram, Twitter and YouTube. It looks beautiful with the bootstraps function. The link opens in a separate tab and the visitor is taken to socialmedia he choose, while the site remains open. It is very comfortable. And above links I placed copyright.

![Footer](/static/images/readme-img/footer.png)

__Detailed post page__

- At the top of the page there is a photo related to the post. On the left side is the author of the post (admin) and the date of publication.

- Also in front of the text there are two buttons for the admin: “Edit post” and “Delete post”, and then there is the text of the post itself.

- If a user wants to delete their own comment, he can click on button delete and it appears window with question if user sure to delete own comment
![Comment Delete](/static/images/readme-img/comment-delete.png)

- After the text in post there is an indication of the sponsor (optional if a sponsor has been added), and then there is a field for comments from registered users and a button to send a comment
![Detailed Post Page](/static/images/readme-img/detailed-post-page.png)
![Comments Field](/static/images/readme-img/comments-field.png)

- When a user has left a comment, the comment awaits admin approval
![Comment Approval](/static/images/readme-img/comment-approval.png)

- I also created 3 fake users to control how comments function works

__History page__

- On this page I have displayed on the left side the statistics of the performances of the Brazilian national team at the World Championships, and on the left side the history of performances at the World Championships
![History Page](/static/images/readme-img/history-page.png)

- And below the statistics is progressbar that shows the total progress from performances at the world cups.      
![Progress Bar](/static/images/readme-img/progress-bar.png)

__About page__

- This page contains brief information about the company, as well as what the company does
![About Page](/static/images/readme-img/about-page.png)

__Add post page__

- On this page, the admin can create posts without going into the admin panel. There are all the necessary fields here, such as: post title, the ability to add a image, description, short description of the post, the ability to add a sponsor and the add post button
![Add Post Page](/static/images/readme-img/add-post-page.png)

__Edit post page__

- On this page, the admin can create posts without going into the admin panel. There are all the necessary fields here, such as: post title, add URL path, ability to add/remove pictures, description, short description of post, ability to add sponsor and update post button
![Edit Post Page](/static/images/readme-img/edit-post-page.png)

__Delete post page__

- When the admin decides to delete a post, he can do this directly from the site by clicking on the delete button located at the beginning of the post. Next comes a transition to a page where confirmation is requested to delete the page. On this page the admin can delete a post.
![Delete Post Page](/static/images/readme-img/delete-post-page.png)

__Sign up page__

- On this page you can register your account by filling out the username, e-mail (optional) and password fields. Then click on the sign up button to create account
![Sign Up Page](/static/images/readme-img/register-account.png)

__Sign in page__

- To log into your account on the site, you need to go to the login page, where you should fill in the username and password fields and click on the sign in button
![Sign In Page](/static/images/readme-img/sign-in-page.png)

__Sign out page__

- The sign out page looks like this: with the possibility of two options, exit or stay on the site
![Sign Out Page](/static/images/readme-img/sign-out-page.png)

__Error 404 page__

- If the user incorrectly specified the page path or clicked on a non-existent page, then he is taken to a 404 page. This page contains a link to return to the main page
![404 Page](/static/images/readme-img/404-page.png)

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

* [Coolors](https://coolors.co/) - Colours palette.

## Testing

To view testing go here [TESTING.md](TESTING.md)

## Deployment

### How to deploy on Heroku

The project was deployed to Heroku in the following manner:

1. Firstly you need to sign up on the Heroku website.
2. There after choose new and "create New App", give the app a name, choose a region: Europe
3. Go to deploy, see Deployment Method and select GitHub.
4. At section "Deployment method", click "GitHub" and connect your account with Heroku.
4. To connect your Heroku app to your code in a Github repository, you need to enter the name of your repository and click on the "Search" button. After that click on button “Connect” when it appears.
5. Go to manual deploy, select the branch from which you want to build your application and click to "Deploy Branch".
6. You have to wait until the app is build. When it wiil be done it will appear an “App was successfully deployed” message and after that you will see a "View" button. When you click on this button you will see your app deployed.

### How to fork

To fork do do the following steps:

1. You have to log in/register on GitHub.
2. Go to the repository for this project [FootBrazil](https://github.com/Askeran17/footbrazil).
3. Click the "Fork" button in the top right corner.

### How to clone

To clone do the following steps:

1. You have to log in/register on GitHub.
2. Go to the repository for this project [Footbrazil](https://github.com/Askeran17/footbrazil).
3. To clone the repository using HTTPS, under "HTTPS", click to copy button. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click to copy button. To clone a repository using GitHub CLI, click GitHub CLI, then click to copy button.
4. Open terminal, change the current working directory to the location where you want the cloned directory.
5. Type git clone, and then paste the URL you copied earlier. Press Enter to create your local clone.

## Credits

I was inspired by the "I Think Therefore I Blog" and "Flask Framework" Rosie project at the Code Institute. I
watch YouTube tutorial about how to edit/delete post from website itself (https://www.youtube.com/watch?v=Y1Us5jVT07E&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=17)

As for the site design I also liked how these projects was done: (https://github.com/davidindub/designland) and (https://github.com/Dhvani-intwala/spice-villa). 

### Content 

- Since there is very little detailed information in the English-language segment about the historical moments of the Brazilian national football team, I took information from Russian-language sites (such as, torcida.com.ru) for my posts and history page. And I translated it into English using Google Translate; I know the Russian language well and therefore did not just copy and paste, but checked and corrected inaccurate places in the translation. I used ready-made text from a Russian site, because the historical details needed to be conveyed exactly as they exist. Therefore, I did not invent these texts myself, but had to convey them to the reader exactly in the form in which they exist.

- The icons was taken from [Font Awesome](https://fontawesome.com/)

### Media

- The images in site I took from torcida.com.ru and open source, i.e. google.