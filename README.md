# Dog Grooming Website

## Introduction
Welcome to Pawfection Parlour. This project is a simplebooking system, allow users to book a slot for this dog groomer. This will use languages such as Django, Python, HTML, CSS and JavaScript.

This project will show the use of CRUD functionality (Create, Read, Update, Delete). The user will be able create, read, update and delete their user profile and bookings.

A live website can be found [here](https://pawfectionparlour.herokuapp.com/).

![website preview](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653677762/amiresponsive_czuaj5.png)

# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
    -   [1.4. Surface](#surface)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Development Cycle](#development-cycle)
-   [6. Deployment](#deployment)
-   [7. End Product](#end-product)
-   [8. Known Bugs](#known-bugs)
-   [9. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)

For this project I wanted to build something close to home. My girlfriend owns a dog grooming business yet doesn't own a website. All of her bookings are made via social media and she adds all her bookings in manually. I wamted to create a system where that can be done via a website. 

his project will showcase simplicity and ease to making a booking, updating a booking, cancelling a booking, creating a personal profile and updating the same profile.

<a name="strategy"></a>

[Go to the top](#table-of-contents)

### Project Goals
The main goal of this project is to allow the user to sign up, sign in/out, create/update a user profile and create/update/delete a booking in a simple and effective process.

### User Goals:
First Time Visitor Goals
-   As a first-time visitor, I want to make a bokking at my chosen date and time.
-   As a first-time visitor, I want to view the servcies available, so that I can decide if this groomer is for me.
-   As a first-time visitor, I want to be able to get the contact details of the groomer with ease.

Returning Visitor Goals
-   As a Returning Visitor, I want to update my booking details.
-   As a Returning Visitor, I want to cancel a booking I have already made.
-   As a Returning Visitor, I want to edit my profile for any future bookings.

### User Expectations:
The system should have a simple user interface, with the navigation to each section clear and concise.

-   The servcies page is clear to read.
-   The user interface is easy to navigate.
-   The website is responsive on all devices.
-   To have the ability to contact the groomer for any enquiries.

### User Stories
Throughout the project I used the GitHub projects board to log all user stories as my project management tool. This helped me keep focus on the necesarry tasks as I would move them to the "in progress lane" as I'm working on the story. I would then move them to the "done" lane once the story has been completed.

![user_story_board](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653677510/User_Stories_To_Do_hmsye6.png)
![user_story_board](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653677764/UserStoriesComplete_lmeffc.png)

### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Display services available | 5 | 5
Account signup | 5 | 5
User profile | 5 | 5
Responsive design | 5 | 5
Contact form | 4 | 5
Ability to create a booking | 5 | 4
Ability to update a booking | 5 | 4
Ability to cancel a booking | 3 | 4
Avoid double bookings | 4 | 1

Total | 41 | 38

## Scope
As I am unable to include all of the features from the strategy table. I will phase this project in multiple phases. Phase 1 will be what I have identified as a minimum viable product. Please find below the plans I have for each phase.

### Phase 1
- Display a services page
- Allow users to register for an account
- Allow users to create and edit a personal profile
- Responsive design
- Contact form
- Ability to create a booking
- Ability to update a booking
- Ability to cancel a booking

### Phase 2
- Avoid double bookings
- Contact form model, so messages are saved to the database
- Email confirmation when a message has been received.
- Account email verification
- Replace django-crispy forms with HTML forms for easier control of validation and styling

<a name="structure"></a>

[Go to the top](#table-of-contents)

It is really important to include responsive design in this project as many users are using different devices (mobile, tablet, laptop/PC). This gives the user the best experience on their device.

- Responsive on all device sizes
- Easy navigation through labelled buttons
- Footer at the bottom of the index page that links to the social media website.
- All elements will be consistent including font size, font family, colour scheme.

### Database Model
Planned database structure:
![database_model](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653679195/database_structure_ucebtf.png)

Final database structure:

```python
class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings"
    )
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-booking_date"]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dog_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return str(self.user)
```

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

Home/Landing Page Desktop:
![home_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681663/wireframehome_q12gtx.png)

Services Page Desktop:
![services_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681665/wireframeservices_wf95l7.png)

Register Page Desktop:
![register_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681661/wireframesignup_j11mzc.png)

Login Page Desktop:
![login_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681661/wireframelogin_bdccry.png)

Online Booking Page Desktop:
![online_booking_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681662/wireframemakebooking_qroecc.png)

Contact Page Desktop:
![contact_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681661/wireframecontact_xsa6u3.png)

Edit Profile Page Desktop:
![edit_profile_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681661/wireframeeditprofile_icfqhw.png)

Manage Booking Page Desktop:
![manage_booking_page_desktop](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681662/wireframemanagebookings_f4l7dz.png)

Mobile Views
![mobile_views](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681799/mobileviewone_tvmgoz.png)

Mobile Views
![mobile_views](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653681799/mobileview2_paojxs.png)


<a name="surface"></a>

## 1.4. Surface

### Colours

After discussing with the groomer, she opted for bg-success with background color of antiquewhite.

### Typography

Groomer decided to use Cinzel + Decorative as my font of choice with Italianno as the backup font for browsers that might not support

The link to the font can be found [here](https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Italianno&display=swap').

<a name="features"></a>

# 2. Features

[Go to the top](#table-of-contents)

### All Pages
- The navigation bar is placed at the top of all pages. The navigation bar is dynamic in that meaning depending on if the user is logged in or not the options will change.
- If the user is not logged in the navigation bar will look like this:
![user_not_logged_in](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653682588/navbarprelogin_cc96ah.png)
- If the user is logged in the navigation bar will look like this:
![user_logged_in](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653682588/navbar_r9bwoi.png)
- The footer is placed at the bottom of each page with social media icons. When hovering over them it creates a zoom effect giving the user more of an experience. These icons will open the links in a new tab.

- The website title is also placed at the top of all pages. Clicking on it will also direct the user to the home page.

### Register Page
- A simple signup form that requires the user to enter a unique email address and a password. The password must be entered again for confirmation, this must match the already entered password above.
- A message to prompt the user that if an account is already been created they can click the sign-in hyperlink to be redirected to the sign-in page.
- If the user enters an email address that has already been registered, the user is prompted by an error message.
![email_validation_error](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653682592/signupemail_iwjh8c.png)
- If the user enters a password that is not secure, the user will be prompted by a message.
![password_too_common](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653682588/passwordcommon_pyvrj3.png)
- If the user enters both passwords that do not match, the user is prompted by a message.
![signup_email_validation](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653682590/samepassword_n5ctzz.png)
- Once the user has successfully signed up, this will automatically log in and direct the user to the create profile page.

### Login Page
- A login form that requires the user to enter their email address and password that they used when signing up to the site.
- A message to prompt the user that if an account has not been created they can click the signup hyperlink to be redirected to the signup page.
- If the user enters in the wrong credentials, a message is displayed to the user.
![signup_email_validation](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653682792/loginzoom_ro6rpu.png)

### Logout Page
- When clicking logout from the navigation bar, the user is redirected to a sign-out page to confirm their action.
![logout_page](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653682877/signoutzoom_o6oi64.png)

### Landing Page
- A simple but cute photo of a groomed dog.
- A book now button that directs the user to create a booking page. If the user has not logged in it will prompt the user to register or log in first.

### Create Profile Page
- Once the user has registered they will be redirected to the create profile page. The page displays a form for the user to enter their first name, last name, dog name and telephone number.

### Edit Profile Page
- The user can navigate to this page by clicking on the edit profile link in the navigation bar. This page will display the current profile details with a form below for the user to update any details.

### Services Page
- All three service options are displayed.

### Contact Page
- An information section that displays the groomers telephone number, email address, opening times and address.
- A contact form that requires the user to enter their full name, email address and a message. The form is already pre-filled with the user's full name (if the user is logged in and has created a profile).
- A Google maps iframe of the groomers location.

### Create Booking Page
- A form that requires the user to enter/select the booking details.
Full name and contact telephone number are prefilled if the user has created a profile.
The user will then need to select a date and time
- The date input field has JavaScript code so the default value is today's date and the user cannot select a date that is previous to today.
- When clicking the make book now button the booking will then be requested to the groomer for approval.
![Make a booking](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653683132/makeabookingzoomed_lphsgy.png)

### Manage Booking Page
- Displays all user-related bookings in a list view within a card.
- Each card will show a booking reference, booking date, booking time, It will also contain a button to change booking details and a cancel booking button.

### Edit Booking Page
- This page will display the current booking details with a form below for the user to update any details.
- When the changes are submitted, the booking will be processed as the booking requested status.

### Cancel Booking
- When the user clicks the cancel booking button they will be redirected to a confirmation page.

<a name="technologies-used"></a>

## 3. Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project uses Bootstrap 5.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
-   [Google Fonts](https://fonts.google.com/)
    -   Google fonts were used to import the "Be Vietnam Pro" font into the style.css file which is used on all pages throughout the project.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.

    <a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)

### Google Developer Tools
For every element that I added to my HTML, I would add the basic CSS to my stylesheet. I would then use the inspect element to try different styles. Once I've got it to my liking I would try to see if I can implement the styling with bootstrap, if I could not replicate the styling I would copy the CSS from google and paste it into my CSS stylesheet. This allows me to keep track of the code I am using.

I also checked the accessibility of the page using lighthouse.
![google_lighthouse](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653683539/lighthouse_mcvgmd.png)

### Responsive Tools
I used [Am I Responsive](http://ami.responsivedesign.is) to make sure that all my pages are responsive to all devices.

### W3C Validator Tools
#### HTML and CSS:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any errors within the HTML pages.

- All errors were minimal eg. Whitespace

### JavaScript:
I used JS Hint to check for any errors within my JavaScript script tags. JS Hint showed warnings on line 1 which was missing a semicolon, however as this was for the script tag I have ignored it. This piece of JavaScript was along copied and pasted from an external source therefore, I have not made any changes to the code.

I had no errors in my JavaScript files.

### Python:
I used [PEP8 online](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653683876/pep8view_gmj7bb.png) to check for any errors within my Python files. The validator showed multiple "expected 2 blank lines.

There were also "line too long" errors within my settings.py file but I have chosen to ignore these as this is a very important file.

## Manual Testing
I have tested my site on Safari and google chrome on multiple devices.

These include:
-   iPhone X
-   iPhone XS Max
-   iPad Pro
-   MacBook Pro

Please find below my testing process for all pages via mobile and web:

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | When clicking the "home" button in the navigation bar, the browser redirects me to the home page. The is active styling will appear as the home button has a red background. | PASS
Services page | When clicking the "Services" button in the navigation bar, the browser redirects me to the services page. 
Contact page | When clicking the "contact" button in the navigation bar, the browser redirects me to the contact page. | PASS
Book now page | When clicking the "book now" button in the navigation bar, the browser redirects me to the book now page.| PASS
Manage booking page | When clicking the "manage bookings" button in the navigation bar, the browser redirects me to the manage booking page. The user will know they are on this page by the heading. | PASS
Edit profile page | Checked foreground information is not distracted by backgrounds| PASS
Register page | When clicking the "register" button in the navigation bar, the browser redirects me to the register page. The user will know they are on this page by the heading. | PASS
Login / Logout page | When clicking the "login" or "logout button in the navigation bar, the browser redirects me to the login or logout page. The user will know they are on this page by the heading. | PASS
Foreground & background colour| PASS
Text | Checked that all fonts and colours used are consistent. | PASS

### Footer
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Facebook | When clicking the Facebook icon, a new tab opens and redirects to the Facebook website. | PASS
Twitter | When clicking the Twitter icon, a new tab opens and redirects to the Twitter website. | PASS
Instagram | When clicking the Instagram icon, a new tab opens and redirects to the Instagram website. | PASS

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

![index_google_lighthouse](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653684267/accessibility_ojwrh1.png)


