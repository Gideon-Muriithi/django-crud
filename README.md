## Django CRUD

A Django crud operations 


## Description

The **django-crud** is the backbone of an application for showcasing crud operations in django framework.
The application provides features for creating, viewing, editing and deleting records.


## Development set up


-   Check that python 3.8.x is installed:

    ```
    python --version
    >> Python 3.8.x
    ```

-   Install pipenv:

    ```
    pip3 install pipenv
    ```

-   Check pipenv is installed:
    ```
    pipenv --version
    >> pipenv, version 2018.11.26
    ```
-   Check that postgres is installed:

    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1
    ```
-  Database
    * Swith to postgres account (in terminal)
        ```
        sudo su - postgres
        ```
    * Run PostgreSQL command line client.
        ```
        psql
        ```
    * Create a database user with a password.
        ```
        CREATE USER san_owner with password 'password12345';
        ```
    * Create a database instance.
        ```
        CREATE DATABASE san_db owner san_owner encoding 'utf-8';
        ```  
    * Login psql as user
        ```
        psql -d san_db -U san_owner
        ```

- Clone the mat-api repo and cd into it
    ```
    git clone URL-----------
    ```
- Create  virtual environment
    ```
    pipenv --python 3.8

    ```
- Turn off a virtual environment  
    ```
    exit
    ```

- Spawn a shell in a virtual environment
    ```
    pipenv shell
    ```
- Install dependencies
    ```
   pipenv install 
    ```
- Create Application environment variables and save them in .env file 
    ```
    DJANGO_READ_DOT_ENV_FILE=True
    DJANGO_DEBUG=True
    DATABASE_URL='postgresql://localhost/mat_db?user=mat_owner&password=password12345'
    SECRET_KEY='super_secret'

- Add the variables in the .env file to path
    ```
    source .env
    ```
- Running migrations

    - Initial migration commands
        ```
        make migrations
        
        make migrate
        ```
    - To create migration for single apps
        ```
        python manage.py makemigrations appName
        ```



- Run application.
    ```
    make serve
    ```

### Merge Request Process

-   A contributor shall identify a task to be done from **link PT board here** 
- If there is a bug , feature or chore that has not been included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
-   The Contributor shall then create a branch off the `master` branch where they are expected to undertake the task they have chosen.
-   After undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
-   If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `development` by the owners of this repository.



## Built with
- Python version  3
- Django
- Postgres
- HTML
- Bootstrap
- CSS
 ```
