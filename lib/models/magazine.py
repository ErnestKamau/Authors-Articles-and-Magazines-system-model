from lib.db.connection import get_connection



conn = get_connection()
cursor = conn.cursor()
class Magazine:
    all = {}
    
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
        
    def __repr__(self):
        return f"<Magazine {self.id}: {self.name}, {self.category} >"
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            return ("Name must be a string")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str):
            self._category = category
        else:
            return ("Category must be a string")
    
    def save(self):
        sql = "INSERT INTO magazines(name, category) VALUES (?, ?)"
        
        cursor.execute(sql, (self.name, self.category))
        conn.commit()
        
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    
    @classmethod
    def instance_from_db(cls, row):
        magazine = cls.all.get(row[0])
        if magazine:
            magazine.name = row[1]
            magazine.category = row[2]
        else:
            magazine = cls(row[1], row[2])
            magazine.id = row[0]
            cls.all[magazine.id] = magazine
        return magazine
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM magazines WHERE id = ?"
        
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name_or_category(cls, name=None, category=None):
        sql = "SELECT * FROM magazines WHERE name = ? OR category = ?"
        
        row = cursor.execute(sql, (name, category)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
    @classmethod
    def article_counts(cls):
        sql = "SELECT magazines.name, COUNT(articles.id) AS article_count FROM magazines LEFT JOIN articles ON magazines.id = articles.magazine_id GROUP BY magazines.id"
        rows = cursor.execute(sql).fetchall()
        return (f"Count is : {len(rows)}")
    

    
    def contributors(self):
        from .author import Author
        sql = "SELECT DISTINCT authors.* FROM authors JOIN articles ON articles.author_id = authors.id WHERE articles.magazine_id = ?"
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Author(id=row[0], name=row[1]) for row in rows]
    
    
    def articles(self):
        from .article import Article
        sql = "SELECT * FROM articles WHERE magazine_id = ?"
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Article(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]
    
    def article_titles(self):
        sql = "SELECT title FROM articles WHERE magazine_id = ?"
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [row[0] for row in rows]
    
    
    def contributing_authors(self):
        from .author import Author
        sql = "SELECT authors.*, COUNT(articles.id) AS article_count FROM authors JOIN articles ON articles.author_id = authors.id WHERE articles.magazine_id = ? GROUP BY authors.id HAVING COUNT(articles.id) > 2"
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Author(id=row[0], name=row[1]) for row in rows]