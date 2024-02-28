# Stock app
This app allows the user to CRUD products and create alerts based on the expiration date of products
## Requirements

-   Python v3.9 or greater
-   Pip v18 or greater
- PostgreSQL 14.0 or greater

## Quick Start 

-   **Make sure you have Python 3.9 or above installed**
    
    -   `python3 --version`
   - **As well as postgres**
    
	    -   `psql --version`

On Windows you might have to use  `python`  without the version (`3`) suffix.

**Installation**
Install all requirements into your virtual env

```
pip install -r requirements.txt

```
Create a database in PostgreSQL named stock
```
psql
CREATE DATABASE stock;
```
Finally, set the enviroment variables for SECRET_KEY and DEBUG

**Run**
Before running the app, run migrations to your local database with
```
python manage.py migrate
```
Then run the app
```
python manage.py runserver
```
## Examples of API uses
**Authentication**
Before trying the following endpoints, you must create an account from the terminal using
```
python manage.py createsuperuser
```
Then sign in from /admin


**Products**
List products
```
GET /api/products/
```
List products filtered by expire date and ordered by expire date
```
GET /api/products/?expires_min=date&expires_max=date&order_by=expires_at=attribute
```
Retrieve data from one product
```
GET /api/products/{id}
```
List alerts from one product
```
GET /api/products/{id}/alerts
```
