# INFORCE TEST TASK

General environmental variables

| variable                   | Description                                  |
|----------------------------|----------------------------------------------|
| 'SECRET_KEY'               | Django secret key                            |
| 'DATABASE_NAME'            | Postgres database name                       |
| 'DATABASE_PORT'            | Postgres port                                |
| 'DATABASE_USER'            | Postgres username                            |
| 'DATABASE_PASSWORD'        | Postgres password                            |
| 'DATABASE_HOST'            | Postgres host                                |




# Commands
Use the following command in terminal to run application: docker-compose up --force-recreate --build

# Run tests
All tests and flake8 are running in separate docker containers and will be automatically applied

# Endpoints
1. GET /employee/ - to list all employee objects
2. POST /employee/create/ - to create new employee object\
REQUEST BODY

| FIELD                      | Type                                         |Description           |
|----------------------------|----------------------------------------------|----------------------|
| 'username'                 | String                                       |Username              |
| 'password'                 | String                                       |Password              |
3. GET /employee/vote_for/?id=<menu_id> - to vote for menu with ID <menu_id>
4. POST /auth/ - to pass authentication and get refresh and access tokens
REQUEST BODY

| FIELD                      | Type                                         |Description           |
|----------------------------|----------------------------------------------|----------------------|
| 'username'                 | String                                       |Username              |
| 'password'                 | String                                       |Password              |
5. GET /restaurant/ - to get list of all restaurants
6. POST /restaurant/ - to create new restaurant object
REQUEST BODY

| FIELD                      | Type                                         |Description           |
|----------------------------|----------------------------------------------|----------------------|
| 'title'                    | String                                       |Title                 |
7. GET /restaurant/menu/ - to get list of all menus
8. POST /restaurant/menu/ - to create new menu
REQUEST BODY

| FIELD                      | Type                                         |Description                       |
|----------------------------|----------------------------------------------|----------------------------------|
| 'title'                    | String                                       |Title                             |
| 'weekday'                  | String                                       |Weekday(e.g Monday, Tuesday etc.) |
| 'restaurant'               | Integer                                      |Restaurant ID                     |
9. GET /restaurant/get_current_day_menus/ - to get list of all current day menus