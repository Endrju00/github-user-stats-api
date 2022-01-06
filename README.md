# github-user-stats-api
## Project overview
Project was created during Allegro Spring TECH e-Xperience. Out of the three tasks I had to choose from, I chose the third one (Software Engineer task) which consisted in creating software allowing for:
* listing of repositories (name and number of stars),
* returning the sum of stars in all repositories,
* listing the most popular programming languages (name, number of code bytes). 

App is deployed on [Heroku](https://github-user-stats-api.herokuapp.com/api/).

#### Project status
[![Django CI](https://github.com/Endrju00/github-user-stats-api/actions/workflows/django.yml/badge.svg)](https://github.com/Endrju00/github-user-stats-api/actions/workflows/django.yml)

## Installation

### On Windows
1. Clone or download repository from [GitHub](https://github.com/Endrju00/github-user-stats-api).
2. Create virtual environment with <code>Python</code> for example using <code>Conda</code>.
> conda create --name allegro python=3.7
3. Proceed on installing new packages.
> Proceed ([y]/n)? y
4. Activate virtual environment.
> conda activate allegro
5. Install prerequisites from <code>requirements.txt</code>.
> (allegro) pip install -r requirements.txt
6. Run tests.
> (allegro) python manage.py test
7. If the output is 'OK' run the <code>api</code>.
> (allegro) python manage.py runserver
8. To see the running application go to [localhost/api](http://127.0.0.1:8000/api)
9. You should see the API Overview page now.

## Example of use
The <code>api</code> supports a few queries:
- <code>\<username\>/repositories/</code> - listing of repositories (name and number of stars),
- <code>\<username\>/sum-of-stars/</code> - returning the sum of stars in all repositories,
- <code>\<username\>/programming-languages/</code> - listing the most popular programming languages (name, number of code bytes).
 
 
### Example:
> http://127.0.0.1:8000/api/allegro/sum-of-stars/

The result should be simmilar to this:
```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "sum_of_stars": 14455
}
```
 
### Format
- To get data in user-friendly format use a query from the example above
 - To get data in <code>JSON</code> format you can add a format parameter <code>/?format=json</code>

### Example:
> http://127.0.0.1:8000/api/allegro/sum-of-stars/?format=json
```
{"sum_of_stars":14455}
```

### Errors
If there is an error on the GitHub API side, the body and the error code will be returned.

```
HTTP 204 No Content
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "info": "User not found",
    "error_code": 404
} 
```
### Error codes
* <code>403</code> - API rate limit exceeded.
* <code>404</code> - User not found.
* <code>408</code> - API Request Timeout.
* <code>500</code> - Different Server Error.
* <code>503</code> - Connection Error.

### HTTP Status codes
 * <code>200</code> - The request succeeded.
 * <code>204</code> - No Content. If there is an error 404 on GitHub API side or User has not public repositories.
 * <code>207</code> - Multi-Status. If there is an error on GitHub API side different than 404.
 * <code>404</code> - Page not found.
 * <code>500</code> - Server Application error.
 
## Deployment
App is deployed on [Heroku](https://github-user-stats-api.herokuapp.com/api/). The way of use is similar to the situation of using the application locally.
> https://github-user-stats-api.herokuapp.com/api/allegro/sum-of-stars/?format=json
```
{"sum_of_stars":14455}
```

## Testing
The application is equipped with tests that can be found in <code>api/tests.py</code> file:
 - <code>test_connection</code> to test connection between client and GitHub API,
 - <code>test_api_overview</code> to test API Overview endpoint,
 - <code>test_user_repositories</code> to test User Repositories endpoint,
 - <code>test_user_stars</code> to test User Sum Of Stars endpoint,
 - <code>test_user_programming_languages</code> to test User Programming Languages endpoint.
 
 To test the application:
 > (allegro) python manage.py test
 
### Continuous Integration
CI is configured to run tests after every push or pull request on main branch. The status badge in [Project overview](#project-overview) shows if tests are passed.

## Project structure
Structure of a project was created by Django framework.
 * <code>api/</code>
   * <code>migrations/</code> - migrations connected with the <code>api</code>
   * <code>admin.py</code> - file used for registering the Django models into the Django administration.
   * <code>apps.py</code> - file used for adding configuration for the app.
   * <code>models.py</code> - represents the models of web applications in the form of classes. 
   * <code>tests.py</code> - tests connected with the <code>api</code>
   * <code>urls.py</code> - file used for adding url configuration of an app.
   * <code>views.py</code> - file used for creating views and endpoints.
 * <code>project/</code>
   * <code>asgi.py</code> - ASGI stands for Asynchronous Server Gateway Interface.
   * <code>settings.py</code> - Django project configuration.
   * <code>urls.py</code> - file used for adding url configuration of a project.
   * <code>wsgi.py</code> - WSGI stands for Web Server Gateway Interface.
 * <code>Procfile</code>, <code>runtime.txt</code> - files needed for deployment.
 * <code>db.sqlite3</code> - sqlite3 file created by Django framework.
 * <code>manage.py</code> - tool for executing Django-specific tasks.
 * <code>requirements.txt</code> - libraries and packages that must be installed for the application to work properly.
 

 
