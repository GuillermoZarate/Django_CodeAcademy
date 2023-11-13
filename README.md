# Web app development projects with Dajngo

This repository stores all the projects developed as part of the "Build Python Web Apps with Django" course. Django, an open-source Python web development framework, enables you to swiftly create web applications. With a plethora of tools already provided by Django, you have the flexibility to pick and choose what you need to get the job done.

Skills gain with this course:

- Apply Python skills for web development.
- Build full-stack web applications.
- Deploy a Django app to the web.


## Projects

Below, the six projects that are part of this course are described along with what is done in each one.

### Project 1: [Fourtenteller](https://github.com/GuillermoZarate/Django_CodeAcademy/tree/main/fortunteller)

- **Project Description:**

  In the "Fortune Teller" project, we will construct a web app that provides users with random positive messages to brighten their day. Leveraging Django's MTV pattern, the website will call a view function upon loading to select a random fortune from a predefined list. This fortune will then be populated into a template and sent back to the client. The project will guide you through building a Django project from scratch, starting with an empty workspace.

- **Steps and Tasks:**
  1. Start the Fortune Teller Project by creating a Django project named "fortuneteller."
  2. Configure the project by navigating to the project folder and running migrations.
  3. Test the project by starting the development server and accessing it through the browser.
  4. Create a new app named "randomfortune" to eventually display fortunes randomly.
  5. Install the new app by adding it to the list of installed apps in the Django project's settings.
  6. Create an HTML template named "fortune.html" within the randomfortune app to format and display fortunes.

### Project 2: [Tourist Attractions](https://github.com/GuillermoZarate/Django_CodeAcademy/tree/main/touristAttractions)

- **Project Description:**

  "Tourist Attractions" is an application that enables users to explore a list of tourist attractions in each state. Users have the flexibility to specify a particular state, gaining access to more detailed information about its attractions. In this project, you will focus on creating templates using Django, incorporating concepts from the templates lesson. This involves extending base templates, integrating static files, and applying filters to variables within the template.

- **Steps and Tasks:**
  1. Create a base template named base.html to establish a common structure for the application.
  2. Add a link in the base template for users to navigate back to the home page.
  3. Implement blocks in the base template for head and content to load assets and display page-specific content.
  4. Develop the homepage (home.html) by extending the base template and styling it with a CSS file.
  5. Add a welcoming message to the homepage and build a table to display attractions and their respective states.
  6. Populate the table with attractions using Django Template Language (DTL) and apply sorting based on the state.
  7. Create a details.html template to display a list of tourist attractions for a specific state.
  8. Extend details.html from the base template, load the CSS sheet, and add a header indicating attractions for the selected state.
  9. Create a table in details.html to list attractions for the selected state, and use DTL to iterate through attractions.
  10. Add conditional logic in the loop to display attractions only for the selected state.


### Project 3: [Djaunty Rent-a-Bike](https://github.com/GuillermoZarate/Django_CodeAcademy/tree/main/djauntyRent-a-bike)

- **Project Description:**

  Djaunty Rent-a-Bike aims to modernize its bike rental system by transitioning from a paper and pencil method to a Django-based model. The focus is on implementing Django models, databases, and CRUD operations. The simplified schema revolves around three main entities: Bike, Renter, and Rental. The project addresses the specific details of each entity, such as bike types, colors, renter information, and rental details.

- **Tasks:**
  1. Plan the schema by examining the provided models.py.
  2. Create the Bike model with fields for bike type and color, implementing a choice option for bike types.
  3. Define the Renter model with fields for first name, last name, phone, and VIP status.
  4. Implement a custom __str__ method for both Bike and Renter models to improve the readability of instances.
  5. Develop the Rental model with foreign keys for Bike and Renter, date, and price fields.
  6. Create a method, calc_price, within the Rental model to calculate the rental price based on specified conditions.
  7. Set up the database schema using migrations.
  8. Populate the database by creating instances of Bike, Renter, and Rental models.
  9. Explore querying methods in the Python shell, including filtering, excluding, and reverse relationships.
  10. Optionally, extend the project by adding extra fields to models or incorporating metadata.


### Project 4: [The Django Djitney](https://github.com/GuillermoZarate/Django_CodeAcademy/tree/main/djangoDjitney)

- **Project Description:**

  The Django Djitney project involves creating a user-friendly site for the Codes-ville Official Department of Transportation to showcase and manage the routes of their new commuter train, the Django Djitney. The application utilizes Django models, views, and URLs to handle information related to jitney lines, stations, and stops. The provided models—Line, Station, and Stop—are interconnected to represent the structure of the commuter train system.

- **Tasks:**
  1. Understand the context by examining the provided models (Line, Station, Stop) and their connections.
  2. Review the existing templates (lines.html, stations.html, stops.html) to understand the required views and URLs.
  3. Explore forms.py to understand how forms will be utilized for creating and updating views.
  4. Navigate to views.py and review the provided code and imports.
  5. Implement views for Lines:
     - Create LinesView (ListView) to display jitney lines.
     - Create CreateLineView (CreateView) for adding new jitney lines.
     - Create UpdateLineView (UpdateView) for modifying existing jitney lines.
     - Create DeleteLineView (DeleteView) for deleting jitney lines.
  6. Test the functionality of the implemented views for Lines in the web browser.
  7. Implement views for Stations:
     - Create StationsView (ListView) to display stations.
     - Create CreateStationView (CreateView) for adding new stations.
     - Create UpdateStationView (UpdateView) for modifying existing stations.
     - Create DeleteStationView (DeleteView) for deleting stations.
  8. Test the functionality of the implemented views for Stations in the web browser.
  9. Implement views for Stops:
     - Create StopsView (ListView) to display stops.
     - Create CreateStopView (CreateView) for adding new stops.
     - Create UpdateStopView (UpdateView) for modifying existing stops.
     - Create DeleteStopView (DeleteView) for deleting stops.
  10. Test the functionality of the implemented views for Stops in the web browser.
  11. Optionally enhance the app:
      - Add a color field to lines and update templates for colored text.
      - Add more fields to a station, such as age or last_cleaned_date.
      - Add a schedule to jitney lines to show the times each train stops at a given station.


### Project 5: [Tourist Attractions with Forms](https://github.com/GuillermoZarate/Django_CodeAcademy/tree/main/touristAttractions)

- **Project Description:**

  The "Tourist Attractions with Forms" project involves creating a Django web application for a local travel agency to manage tourist attractions and states. The goal is to allow users to add new attractions and states dynamically using forms. The project covers generic form creation, creating instances using forms, and ensuring form security.

- **Tasks:**
  1. Examine the changes in models.py, noting the addition of verbose_name arguments for field display in generic forms.
  2. Create forms.py and import forms from django and the State and Attraction models from .models.
  3. Create StateCreateForm and AttractionCreateForm classes in forms.py, inheriting from forms.ModelForm.
  4. Define Meta classes within StateCreateForm and AttractionCreateForm to specify the model and fields.
  5. Import StateCreateForm and AttractionCreateForm in views.py, along with CreateView.
  6. Create StateCreate class (CreateView) in views.py, specifying model, form_class, and template_name properties.
  7. Create AttractionCreate class (CreateView) in views.py, following the same pattern as StateCreate.
  8. Update urls.py to include paths for creating states and attractions, linking to the respective views.
  9. Create templates for creating states (state_create_form.html) and attractions (attraction_create_form.html) inside templates/tourist_attractions/.
  10. Extend templates from "tourist_attractions/base.html," load static, and create content blocks for each template.
  11. Add *h1* and *form* elements to templates to display form headers and form inputs.
  12. Update the template_name fields in StateCreate and AttractionCreate views to reference the respective templates.
  13. Add get_absolute_url() method to the State and Attraction models in models.py, returning to the home page ("/tourist_attractions/").
  14. In home.html, add links to the State and Attraction forms using the {% url %} template tag.
  15. Test the application by creating states and attractions and verifying redirection to the home page.
  16. Optionally, add more fields to the models in models.py and update the forms to include them.


### Project 6: [Weekly Dessert](https://github.com/GuillermoZarate/Django_CodeAcademy/tree/main/weeklyDessert)

- **Project Description:**

  The "Weekly Dessert" project involves building a Django web application for a school cafeteria's dessert voting system. The application allows authenticated users to vote for their favorite dessert each week. The project focuses on implementing authentication, creating user accounts, securing paths, and using Django's admin interface to manage data.

- **Tasks:**
  1. Explore the provided code and models structure in the Django project for the weekly dessert application.
  2. Create a superuser using the Python terminal and access the Django admin interface to manage data.
  3. Import the Week and Choice models in admin.py and register them to appear on the /admin page.
  4. Test the registration of models by creating a new dessert through the Choice model in the admin interface.
  5. Open the Python shell and import the User model, then create a new user object with credentials.
  6. Update urls.py to include Django's built-in authentication views for login, logout, and password change.
  7. Modify the login.html template to render form fields for username and password.
  8. Create a SignUp class-based view in views.py using CreateView, UserCreationForm, and "registration/signup.html".
  9. Add a path for user registration in urls.py using the SignUp view and assign a name attribute.
  10. Test user registration by navigating to /signup, completing the form, and logging in.
  11. Import the logout function in views.py and create a logout view function, redirecting users to the index page.
  12. Add a path for user logout in urls.py, use the logout view, and assign a name attribute.
  13. Create a logout button in header.html, linking to the logout path.
  14. Secure paths by importing login_required decorator, applying it to index and vote views.
  15. Import LoginRequiredMixin and apply it to DetailsView and ResultsView class-based views for path security.
  16. Verify the security measures by ensuring only authenticated users can access the home and voting pages.
  17. Optionally experiment with rendered forms, add options in the admin interface, and customize SignUp view fields.
  18. Secure other paths using the LoginRequiredMixin for class-based views.
  19. Ensure the app is secured, allowing only authenticated and logged-in users to access it.
  20. Review the project and optional challenges, experiment with form rendering, and add additional user fields to SignUp view.


## Recursos Adicionales
- [Enlace al curso de CodeAcademy](https://www.codecademy.com/enrolled/paths/build-python-web-apps-with-django)
- [Documentación de Django](https://docs.djangoproject.com/)
- [Repositorio oficial de Django](https://github.com/django/django)

