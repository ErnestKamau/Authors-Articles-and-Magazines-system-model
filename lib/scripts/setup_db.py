from lib.db.connection import get_connection

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    with open("lib/db/schema.sql", "r") as file:
        sql = file.read()
        
        cursor.executescript(sql)
        conn.commit()
        conn.close()


if __name__ == "__main__":
    setup_db()
    print("DB created succesfully!")
    

