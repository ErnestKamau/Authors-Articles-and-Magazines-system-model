# Authors-Articles-and-Magazines-system-model
Models a publishing domain consisting of **Authors**, **Articles**, and **Magazines** using raw SQL with Python classes. It showcases how to represent many-to-many relationships without using an ORM like SQLAlchemy
It is a simple Python backend application that models the relationship between Authors, Articles, and Magazines, with data persisted in a SQL database. In this domain:
- An `Author` can write many `Articles`
- A `Magazine` can publish many `Articles`
- An `Article` belongs to both an `Author` and a `Magazine`
- The `Author`-`Magazine` relationship is many-to-many


## ⚙️ Setup Instructions
Choose one of the following environments:

### Using Pipenv (Install dependencies)
- pipenv install pytest sqlite3
- pipenv shell

## Running the Project
# 1. Initialize the Database
This creates tables from schema.sql. :
- python3 lib.scripts.setup_db

# 2. Seed the Database with Sample Data
- python3 -m lib.db.seed

# 3. Run Sample Queries
To test queries and see example outputs:
 - python3 -m lib.scripts.run_queries


## Model Responsibilities
# Author (models/author.py)
- save(), find_by_id(), find_by_name(), articles(), magazines(), topic_areas(), add_article(magazine, title)

# Article (models/article.py)
- save(), find_by_id(), find_by_title()
- Relationships to authors and magazines

# Magazine (models/magazine.py)
- save(), find_by_id(), find_by_name()
- articles(), contributors(), article_titles(), contributing_authors()





AUTHOR
GitHub: @ErnestKamau
Ernest Kamau
