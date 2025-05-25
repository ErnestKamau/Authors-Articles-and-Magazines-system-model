from lib.models import Author, Article, Magazine
from lib.db.connection import get_connection

conn = get_connection()
cursor = conn.cursor()


def run():
    author = Author.find_by_id(1)
    magazine = Magazine.find_by_id(1)
    article = Article.find_by_id(1)
    
    if author:
        print(f"Author: {author.name}")
        
        print("Magazines:")
        for mag in author.magazines():
            print(f"- {mag.name} ({mag.category})")

        print("Topic Areas:")
        print(author.topic_areas())

    else:
        print("Author not found.")
        
    if magazine:
        print(magazine)
        
        print(magazine.article_counts())
        
        print(magazine.contributors())
        
        print(magazine.articles())
        
        print(magazine.contributing_authors())
        
        print(magazine.article_titles())
    else:
        print("Magazine not found!")
        
    if article:
        print(article)
        
        print(article.magazines())
        
    
        


if __name__ == "__main__":
    run()