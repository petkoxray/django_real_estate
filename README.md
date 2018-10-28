# Simple real estate listing site built with Django
***

### Functionalities
- Authentication (register, login)
- Users can make inquiries for listings
- Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
- and much more...
## Installation

#### Prerequisites

  - Python >= 3.6
  - Postgres for database
#### Steps

```sh
git clone https://github.com/petkoxray/django_real_estate
cd django_real_estate
python3 -m venv venv
source venv/bin/activate (Linux, Mac) or venv/Scripts/activate (Windows)
pip install -r requirements.txt
create .env file from example.env
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
