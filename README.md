# stocks-api-ab-nk

This is a Flask api, stocks-api-ab-nk, that receives a pull request from TD Ameritrade's API.
Functionality: 
1. Data requested from TD Ameritrade will include historic price data.

https://developer.tdameritrade.com/price-history/apis/get/marketdata/%7Bsymbol%7D/pricehistory
https://developer.tdameritrade.com/content/getting-started

2. The data is stored in a PostgreSQL database along with the pull instructions.

3. stocks-api-ab-nk has CRUD operations to withdraw the data and retrieve it at will.

4. The data is saved for each user and the data can be downloaded whenever.

5. The app is deployed via Heroku.

### TODO - @Ale can you add step-by-step instructions for downloading the data?
### I will once we get to that step haha. Not Sure how to pull data in yet without a front end framework but I know it can be done

### Initialization

1. Create your own virtual environment, or use a virtualenv of your choice.

```
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Flask
`pip install Flask`

3. Create folders static (images and css) and templates (html). Add __init__.py, routes.py

4. Install project requirements for installation of dependencies of the project.
https://packaging.python.org/discussions/install-requires-vs-requirements/
`pip install -r requirements.txt`

5. Install Flask-WTF for creating login forms. This install should install WTForms (Flask-WTF dependency) which is used for fields and validators.
https://flask-wtf.readthedocs.io/en/stable/quickstart.html#creating-forms
https://wtforms.readthedocs.io/en/2.3.x/
`pip install Flask-WTF`

8. Install email-validator to validate emails
`pip install email-validator`

6. Install Flask-SQLAlchemy to be used as SQLAlchemy. SQAlchemy is used as a relational mapper for SQL and database acces to PostgreSQL. Used for db.session in __init__.py as if it was SQAlchemy. 
`pip install Flask-SQLAlchemy`

7. Install Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. Used for db.migration in __init__.py. Alembic is a lightweight database migration tool for usage with the SQLAlchemy
`pip install Flask-Migrate`

9. Install psycopg. Psycopg is a PostgreSQL database adapter used in .env to connect to PG Admin URI. It gives credentials to access PG Admin.
Read 31.1.1.2. Connection URIs in:
https://www.postgresql.org/docs/9.2/libpq-connect.html#LIBPQ-CONNSTRING
`pip install psycopg2` or for macs: `pip install psycopg2-binary`

10. Install python-dotenv to read key-value pairs from the .env file.
https://pypi.org/project/python-dotenv/
`pip install python-dotenv`

11. Create .env file to add PG Admin credentials in the following format: DATABASE_URL=postgresql+psycopg2://postgres:yourpasswordhere@127.0.0.1:5432/databasehere 
This will be included in .gitignore

12. Set up Config variables for the Flask app in config.py

13. Create forms.py and add login/signup forms. Create those HTML/CSS files as well and add those routes to routes.py.

14. Create models.py to add models for the back end database. It contains essential fields and behaviors of the data stored in PostgreSQL. Add models to routes.py in signup. Include the following:
```
user = User(email, password = password)

db.session.add(user)
db.session.commit()

return redirect(url_for('signin'))
```

15. Use the following commands once models are added to routes.py. This will make a table in PostgreSQL from the fields added in models.py.
```
$ flask db init
$ flask db migrate -m "Initial migration" # can add any message here
$ flask db upgrade
```

16. Make sure databases are added and signup using any email to make sure the user is added to the database.