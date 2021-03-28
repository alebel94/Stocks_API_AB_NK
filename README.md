# stocks-api-ab-nk

This is a Flask api, stocks-api-ab-nk, that recieves a pull request from TD Ameritrade's API.

Data requested from TD Ameritrade will include historic price data.

The data is stored in a PostgreSQL database along with the pull instructions.

stocks-api-ab-nk has CRUD operations to withdraw the data and retrieve it at will.
