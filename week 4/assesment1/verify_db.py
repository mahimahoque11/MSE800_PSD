import sqlite3

try:
    conn = sqlite3.connect('moneyexchange.db')
    cursor = conn.cursor()
    
    # Query the internal schema table
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("--- Database Verification ---")
    if tables:
        print(f"Success! Found {len(tables)} tables:")
        for table in tables:
            print(f" - {table[0]}")
    else:
        print("No tables found. Check your SQL script.")
        
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")