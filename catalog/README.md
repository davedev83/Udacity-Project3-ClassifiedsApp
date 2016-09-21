# Udacity Full-Stack Nanodegree
### Project 3: Item Catalog - By David Castro

##### Project Overview
---

ClassifiedsApp is a simple python classfieds app that allows a user to create categories and listsings. Users are allowed to edit or delete their own categories and listings. Users can create and account and login via facebook's or google's login interface.

##### Requirements
---

  - Vagrant
  - python
  - sqlalchemy
  - flask

##### How to run
---
- run ```python project.py```
- With a browser visit http://localhost:8000
- Login via facebook or google

##### Reset data
---
The application already includes a sample database (classifieds.db) with basic categories and listings. If you want to reset the data, follow this steps:
- exit the current python instance
- delete the classifieds.db file
- run ```python database_setup.py```
- run ```python addcategories.py```
- run ```python project.py```

##### Get data in JSON format
---
You can get listings by a single category in JSON format by visiting the following page:
- http://localhost:8000/classifieds/category/{category_id}/JSON

You can also get a single listing in JSON format by visiting the following page:
- http://localhost:8000/classifieds/item/{item_id}/JSON

