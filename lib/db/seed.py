from lib.db.connection import get_connection

conn = get_connection()
cursor = conn.cursor()

def seed_data():
    cursor.executescript("""
    DELETE FROM articles;
    DELETE FROM authors;
    DELETE FROM magazines;
    """)


    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Tevin Karanja",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Fred Mwaniki",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Anthony Kamau",))
    

    
    magazine_col = "INSERT INTO magazines (name, category) VALUES (?, ?)"
    cursor.execute(magazine_col, ("Tech Today", "Technology"))
    cursor.execute(magazine_col, ("Health Weekly", "Health"))


    articles_col = "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)"
    cursor.execute(articles_col, ("AI in 2025", 1, 1))
    cursor.execute(articles_col, ("The Future of VR", 1, 1))
    cursor.execute(articles_col, ("Staying Fit at Home", 2, 2))
    cursor.execute(articles_col, ("Data Science with Python", 1, 1))


    conn.commit()
    print("Seeded database successfully.")

if __name__ == "__main__":
    seed_data()
