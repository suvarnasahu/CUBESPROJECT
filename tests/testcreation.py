import wufooform


def test_table_creationmethod():
    conn = wufooform.create_database("test.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS WUFOO;")
    wufooform.create_wufootable(conn)
    data = {"EntryId": "1", "Field4": "Miss.", "Field5": "Suvarna", "Field6": "Sahu", "Field107": "XYZ",
            "Field108": "Sahu", "Field109": "ssahu@student.bridgew.edu", "Field110": "http://sahu.com",
            "Field111": "7816927488", "Field112": " Course Project", "Field113": "Guest Speaker", "Field114": "",
            "Field115": "Job Shadow", "Field116": "", "Field117": "", "Field118": "", "Field417": "",
            "Field418": " Fall 2023 (September 2023- December 2023)", "Field419": "", "Field420": "",
            "DateCreated": "2023-01-26 00:11:29", "CreatedBy": "public", "DateUpdated": "", "UpdatedBy": "null"}
    wufooform.insert_data(conn, data)
    cursor.execute("select * from  'WUFOO';")
    entity_list = cursor.fetchall()
    print('Number of records retrieved: ', len(entity_list))
    print(entity_list)
    assert len(entity_list) == 1
    conn.close()


test_table_creationmethod()
