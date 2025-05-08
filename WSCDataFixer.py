import sqlite3
import csv
import os

#version wsc 9.8+

#main func
def sexymexy(db_path, csv_folder='csv'): #in script dir /csv
    conn = sqlite3.connect(db_path) #connect
    cursor = conn.cursor()
    print("start")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
   
   #create dir if don't found
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)
        return
    
    for filename in os.listdir(csv_folder):
        if filename.endswith('.csv'):
            table_name = filename[:-5].capitalize()
            
            if table_name in tables:
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns = [column[1] for column in cursor.fetchall()]
                
                name_column = None
                possible_names = {'name', 'Name', 'NAME'}
                for col in columns:
                    if col in possible_names:
                        name_column = col
                        break
                
                if not name_column:
                    continue
                
                with open(os.path.join(csv_folder, filename), 'r', encoding='utf-8') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    update_sql = f"UPDATE {table_name} SET {name_column} = ? WHERE id = ?" #query. 
                    
                    for row in csv_reader:
                        if len(row) >= 2:
                            try:
                                cursor.execute(update_sql, (row[1], row[0])) #update tables
                            except sqlite3.Error:
                                pass
    print("Done, Settings edit himself")
    conn.commit()
    conn.close()

print("CREATED BY @silencode")
print("github.com/blitchcore") 
db_path = 'datapack.db' #path to db (in script directory)
sexymexy(db_path) #start