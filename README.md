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
    - [Database](#database)
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

![Six Posts](/static/images/readme-img/six-posts.png)

__Footer__

- In the footer I have placed a link to Facebook, Instagram, Twitter and YouTube. It looks beautiful with the bootstraps function. The link opens in a separate tab and the visitor is taken to socialmedia he choose, while the site remains open. It is very comfortable. And above links I placed copyright.

![Footer](/static/images/readme-img/footer.png)

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

To view testing go here [TESTING.md](TESTING.md)

## Deployment

### Local Development

Deployed using Heroku

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

I was inspired by the "I Think Therefore I Blog" and "Flask Framework" Rosie project at the Code Institute.

### Content 

- All content for the site was written by myself.

- The icons was taken from [Font Awesome](https://fontawesome.com/)

### Media

- The images in site I took from open source, i.e. google.