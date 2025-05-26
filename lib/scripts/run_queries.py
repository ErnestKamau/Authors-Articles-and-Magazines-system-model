from lib.models import Author, Article, Magazine
from lib.db.connection import get_connection
from lib.controllers.__init__ import add_author_with_articles


conn = get_connection()
cursor = conn.cursor()


def run():
    articles = [
        {"title": "12 Keys to Write Senior-Level Tests"},
        {"title": "Passwords have problems, but passkeys have more"}
        ]
    magazines = [
        {"name": "Tech Advisor", "category": "Technology"},
        {"name": "2600: The Hacker Quarterly", "category": "Technology"}
    ]
    add_author_with_articles("Adrian Githae", articles, magazines)
    
   
    author = Author.find_by_id(1)
    magazine = Magazine.find_by_id(1)
    article = Article.find_by_id(1)
    
    if author:
        print (author.name)
        
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