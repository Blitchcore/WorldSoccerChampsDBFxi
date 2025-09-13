import sqlite3

#Created By BLITCHCORE 
#github.com/blitchcore/

def abc(db_path, query):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute(query)
        conn.commit()
        
        changes = cursor.rowcount
        print(f"Успешно обновлено {changes} записей.")
        
    except sqlite3.Error as e:
        print(f"er: {e}")
    finally:
        if conn:
            conn.close()
print("github.com/blitchcore") 
print("/nDefault DB Name = datapack.db")
path = input("void db name: ")  # dbname
if not path:
    path = "datapack.db"
query = input("Void Query: ") #query
abc(path, query)