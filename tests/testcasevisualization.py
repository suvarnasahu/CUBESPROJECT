"""
Check for user creation and correct data for first name, lat name, title and department are fetched from table
"""

import sqlite3

# Define database connection
conn = sqlite3.connect('wufuform.db')
c = conn.cursor()

# Create test user
c.execute('DELETE FROM FACULTY WHERE bsu_email = "ssahu@student.bridgew.edu"')  # delete user if already exists
conn.commit()
c.execute('INSERT INTO FACULTY(bsu_email, first_name, last_name, title, department) VALUES (?, ?, ?, ?, ?)',
          ('ssahu@student.bridgew.edu', 'Suvarna', 'Sahu', 'Mrs', 'BSU'))
conn.commit()

# Test case: Populate data for existing user
c.execute('SELECT * FROM FACULTY WHERE bsu_email = "ssahu@student.bridgew.edu"')
result = c.fetchone()
if result:
    # If user already exists, populate the rest of the data
    first_name = result[1]
    last_name = result[2]
    title = result[3]
    department = result[4]

    # Check that the data was populated correctly
    assert first_name == 'Suvarna'
    assert last_name == 'Sahu'
    assert title == 'Mrs'
    assert department == 'BSU'
else:
    print('User not found in database.')
print("test successfull")
# Close database connection
c.close()
conn.close()
