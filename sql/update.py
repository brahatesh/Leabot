import sqlite3
conn = sqlite3.connect("sqlite.db")

conn.execute('''
    update student set st_name='ram1' where st_id=0
''')

conn.commit()
conn.close()