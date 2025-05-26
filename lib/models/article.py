from lib.db.connection import get_connection


conn = get_connection()
cursor = conn.cursor()


class Article:
    all = {}
    
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id
        
    def __repr__(self):
        return (
            f"<Article {self.id}: {self.title}, " + f"Author ID: {self.author_id}, " + f"Magazine ID: {self.magazine_id}> "
        )
        
    def save(self):
        sql =" INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) "
        
        cursor.execute(sql, (self.title, self.author_id, self.magazine_id))
        
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
        conn.commit()
        
    @classmethod   
    def instance_from_db(cls, row):    
        article = cls.all.get(row[0])
        if article:
            article.name = row[1]
        else:
            article = cls(row[1], row[2], row[3])
            article.id = row[0]
            article.title = row[1]
            article.author_id = row[2]
            article.magazine_id = row[3]
            
            cls.all[article.id] = article
        return article
        
        
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM articles WHERE id = ?"
        
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None 
    
    @classmethod
    def find_by_title(cls, title):
        sql = "SELECT * FROM articles WHERE title = ?"
        row = cursor.execute(sql, (title,)).fetchone()
        
        return cls.instance_from_db(row) if row else None
    
     
    @classmethod
    def all_articles(cls):
        sql = "SELECT * FORM articles"
        
        rows = cursor.execute(sql).fetchall()
        
        return [cls(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]
    
    
    def author(self):
        from .author import Author
        sql = "SELECT * FROM authors WHERE id = ?"
        
        row = cursor.execute(sql, (self.author_id,)).fetchone()
        
        return Author(id=row[0], name=[row[1]]) if row else None
    
        
    def magazines(self):
        from .magazine import Magazine
        sql = "SELECT * FROM magazines WHERE id = ?"
        
        row = cursor.execute(sql, (self.magazine_id,)).fetchone()
        
        return Magazine(id=row[0], name=row[1], category=row[2]) if row else None