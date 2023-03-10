import sqlite3


def testfacultydatabase():
    # Connect to the database
    conn = sqlite3.connect('wufuform.db')
    cursor = conn.cursor()

    # Select data from the customers table
    cursor.execute('SELECT * FROM FACULTY limit 1')
    result = cursor.fetchone()

    # Check if any rows are returned
    assert result is not None
    print('success')

    # Close the database connection
    conn.close()


testfacultydatabase()
