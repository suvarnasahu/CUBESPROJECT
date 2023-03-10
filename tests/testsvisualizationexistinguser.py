import sqlite3

# Define database connection
conn = sqlite3.connect('wufuform.db')
c = conn.cursor()

# Test case: Check existing user
c.execute('SELECT * FROM FACULTY WHERE bsu_email = "ssahu@student.bridgew.edu"')
result = c.fetchone()
if result:
    assert result[1] == 'Suvarna'
    assert result[2] == 'Sahu'
    assert result[3] == 'Mrs'
    assert result[4] == 'BSU'
    
conn.close()
print("Success")
