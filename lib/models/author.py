from lib.db.connection import get_connection



conn = get_connection()
cursor = conn.cursor()


class Author:
    all = {}
    
    def __init__(self, name, id=None):
        self.id = id
        self._name = name
         
        
    def __repr__(self):
        return f"<Author {self.id}: " + f"{self.name} >"
        
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            return ("name must be a string")
        
        
        
    def save(self):
        sql = "INSERT INTO authors(name) VALUES (?)"

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (self.name,),)
        conn.commit()
        
        
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod   
    def instance_from_db(cls, row):    
        author = cls.all.get(row[0])
        if author:
            author.name = row[1]
        else:
            author = cls(row[1])
            author.id = row[0]
            cls.all[author.id] = author
        return author
    
    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM authors WHERE name = ?"
        
        row = cursor.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM authors WHERE id = ?"
        
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None



    def articles(self):
        from .article import Article
        sql = " SELECT * FROM articles WHERE author_id = ?"
        
        rows = cursor.execute(sql, (self.id,)).fetchall()

        return [Article(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]
    
    
    def article_titles(self):
        sql = "SELECT title FROM articles WHERE author_id = ?"
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [row[0] for row in rows]
    

    def magazines(self):
        from .magazine import Magazine
        sql = "SELECT DISTINCT magazines. * FROM magazines JOIN articles ON articles.magazine_id = magazines.id WHERE articles.author_id = ?"
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Magazine(id=row[0], name=row[1], category=row[2]) for row in rows]
        

    def add_article(self, magazine, title):
        from .article import Article
        article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article

    def topic_areas(self):
        return list(set(mag.category for mag in self.magazines()))
    
    
    @classmethod
    def author_with_most_articles(cls):
        sql = "SELECT authors.*, COUNT(articles.id) AS article_count FROM authors JOIN articles ON authors.id = articles.author_id GROUP BY authors.id ORDER BY article_count DESC LIMIT 1"
        row = cursor.execute(sql).fetchone()
        
        return cls(id=row[0], name=row[1]) if row else None
        
        
    
        
        
        
    
        
    
        
        
        