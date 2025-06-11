import sqlite3

def abc(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("UPDATE Club SET bteamof = 0 WHERE bteamof != 0 AND bteamof != -1")
        conn.commit()
        
        changes = cursor.rowcount
        print(f"Успешно обновлено {changes} записей.")
        
    except sqlite3.Error as e:
        print(f"er: {e}")
    finally:
        if conn:
            conn.close()

path = input("void db name: ")#dbname
abc(path)