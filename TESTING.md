## Testing

Throughout the development of the site, I used Google's developer tools to identify and fix any problems along the way.

If something didn't work correctly, I also used Google's developer tools to tweak and fix the problem.

I've thoroughly tested each page using Google Chrome's developer tools to ensure each page is responsive on a variety of screen sizes and devices.

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

The site showed good scores.

<br>

Home page
<br>

![Home](/static/images/readme-img/desktop-index.png)

Detailed Post page
<br>

![Full post](/static/images/readme-img/desktop-full-post.png)

History page
<br>

![History](/static/images/readme-img/desktop-history.png)

About page
<br>

![About](/static/images/readme-img/desktop-about.png)

### Mobile Results

The site showed good scores.

<br>

Home page
<br>

![Home](/static/images/readme-img/mobile-index.png)

Detailed Post page
<br>

![Full post](/static/images/readme-img/mobile-full-post.png)

History page
<br>

![History](/static/images/readme-img/mobile-history.png)

About page
<br>

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

#### Edit post page

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Admin can edit post from website itself | Access to the edit post page after clicked on button "edit" from post | Being able to update the fields, send it and post will be updatet on homepage directly | PASS |

#### Delete post page

| Testing  | Steps | Expected Result | Grade |  
| - | - | - | - |
| Admin can delete post from website itself | Access to the delete post page after clicked on button "delete" from post | Being able to delete post directly | PASS |

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

#### Admin panel

| Testing  | Steps | Expected Outcome | Grade |  
| - | - | - | - |
| Superusers features | Superuser will be able to create, delete and update | Superuser can create, delete and update content | PASS |


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffootbrazil-a7d96ef49755.herokuapp.com%2F)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2Ffootbrazil-a7d96ef49755.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1)

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