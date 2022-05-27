# Dog Grooming Website

## Introduction
Welcome to Pawfection Parlour. This project is a simplebooking system, allow users to book a slot for this dog groomer. This will use languages such as Django, Python, HTML, CSS and JavaScript.

This project will show the use of CRUD functionality (Create, Read, Update, Delete). The user will be able create, read, update and delete their user profile and bookings.

A live website can be found [here](https://res.cloudinary.com/dkxv7amyg/image/upload/v1653677762/amiresponsive_czuaj5.png).

![website preview]()

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