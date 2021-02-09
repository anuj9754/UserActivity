To run locally, do the usual:

1. Create a Python 3.6 virtualenv

2. Install dependencies::

    pip install -r requirement.txt

3. Migrate Code:
    ./manage.py migrate
    
4. Populate the dump dat::

    ./manage.py populate
    
5. Run the Server:
    ./manage.py runserver

6. View the site at http://localhost:8000/
