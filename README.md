# stocks-api-ab-nk

This is a Flask api, stocks-api-ab-nk, that receives a pull request from TD Ameritrade's API.

Data requested from TD Ameritrade will include historic price data.

The data is stored in a PostgreSQL database along with the pull instructions.

stocks-api-ab-nk has CRUD operations to withdraw the data and retrieve it at will.

The data is saved for each user and the data can be downloaded whenever.

The app is deployed via Heroku.

### Initialization

1. Create your own virtualenvironment, or use a virtualenv of your choice.

```
python3 -m venv .venv
source .venv/bin/activate
```

2. Install project requirements

`pip install -r requirements.txt`
