import sqlite3

# Define database connection
conn = sqlite3.connect('wufuform.db')
c = conn.cursor()

# Test case 1: Create new user
c.execute('DELETE FROM FACULTY WHERE bsu_email = "testemail@gmail.com"')  # delete user if already exists
c.execute('INSERT INTO FACULTY VALUES (?, ?, ?, ?, ?)', ('testemail@gmail.com', 'test', 'email', 'Mrs', 'BSU'))
conn.commit()
print("testcase1success")

# Test case 2: Check existing user
c.execute('SELECT * FROM FACULTY WHERE bsu_email = "testemail@gmail.com"')
result = c.fetchone()
if result:
    assert result[1] == 'test'
    assert result[2] == 'email'
    assert result[3] == 'Mrs'
    assert result[4] == 'BSU'
    c.execute('DELETE FROM FACULTY WHERE bsu_email = "testemail@gmail.com"')
    conn.commit()
conn.close()
