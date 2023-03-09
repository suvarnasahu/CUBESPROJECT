import json
from sqlite3 import Connection
import requests
import uvicorn
from fastapi import FastAPI

from secrets import username, password, base_url, formhashkey
import sqlite3


def getentries(uri):
    """
    fetch entries from the wufoo form using uri
    :param uri: api call for wufoo form
    :return: list of entries as json
    """
    response = requests.get(uri, auth=(username, password))
    entries = response.json()
    return entries["Entries"]


def create_database(dbname):
    """
    create a database
    :return: Cursor to the database connection
    """
    conn = sqlite3.connect(dbname)
    print("Connected to Database {} ".format(dbname))
    return conn


def create_wufootable(conn):
    """
    create wufoo table inside database
    :param conn: connection to the database
    :return:
    """
    cursor = conn.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS WUFOO(DateCreated VARCHAR(255),
    DateUpdated VARCHAR(255),
    EntryId INTEGER,
    TITLE VARCHAR(255),
    ORGANIZATION_NAME VARCHAR(255),
    EMAIL VARCHAR(255),
    ORGANIZATION_WEBSITE VARCHAR(255),
    PHONE_NUMBER VARCHAR(255),
    OPP_1 VARCHAR(255),
    OPP_2 VARCHAR(255),
    OPP_3 VARCHAR(255),
    OPP_4 VARCHAR(255),
    OPP_5 VARCHAR(255),
    OPP_6 VARCHAR(255),
    OPP_7 VARCHAR(255),
    PREFIX VARCHAR(255),
    SUMMER2023 VARCHAR(255),
    FALL VARCHAR(255),
    SPRING VARCHAR(255),
    SUMMER2024 VARCHAR(255),
    FIRSTNAME VARCHAR(255),
    LASTNAME VARCHAR(255),
    Updated_By VARCHAR(255));
    """
    cursor.execute(table)

    print("table WUFOO is created")


def insert_data(conn, i):
    """
    inserts form entries to the wufoo table
    :param conn: connection to the database
    :param i: 1 record of entry
    :return:
    """
    cursor = conn.cursor()
    query = """
    INSERT INTO WUFOO(DateCreated,DateUpdated,EntryId,TITLE,ORGANIZATION_NAME,EMAIL,
    ORGANIZATION_WEBSITE,PHONE_NUMBER,OPP_1,OPP_2,OPP_3,OPP_4,OPP_5,OPP_6,OPP_7,PREFIX,
    SUMMER2023,FALL,SPRING,SUMMER2024,FIRSTNAME,LASTNAME,Updated_By)
    VALUES ('{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
    '{}','{}','{}','{}','{}','{}','{}');
    """.format(str(i["DateCreated"]), i["DateUpdated"], i["EntryId"], i["Field107"], i["Field108"], i["Field109"],
               i["Field110"],
               i["Field111"], i["Field112"], i["Field113"], i["Field114"], i["Field115"], i["Field116"], i["Field117"],
               i["Field118"],
               i["Field4"], i["Field417"], i["Field418"], i["Field419"], i["Field420"], i["Field5"], i["Field6"],
               i["UpdatedBy"])
    cursor.execute(query)
    conn.commit()
    print("inserted 1 record")


def showalldbentries(conn):
    cursor = conn.cursor()
    cursor.execute("select * from wufoo")
    entity_list = cursor.fetchall()
    print('Number of records retrieved: ', len(entity_list))
    print(entity_list)
    for k, v in enumerate(entity_list):
        print(k, v)


def returnalldbentries(conn):
    cursor = conn.cursor()
    cursor.execute("select * from wufoo")
    entity_list = cursor.fetchall()
    return entity_list


def returnguientries(conn):
    cursor = conn.cursor()
    cursor.execute("select EntryId,'OrgName:',ORGANIZATION_NAME,'Name:',FIRSTNAME,LASTNAME from wufoo")
    entity_list = cursor.fetchall()
    return entity_list


def getentry(conn, entryid):
    cursor = conn.cursor()
    query = "SELECT EntryId,PREFIX,TITLE,ORGANIZATION_NAME,ORGANIZATION_WEBSITE,FIRSTNAME,LASTNAME, EMAIL," \
            "PHONE_NUMBER,OPP_1,OPP_2,OPP_3,OPP_4,OPP_5,OPP_6,OPP_7," \
            "SUMMER2023,FALL,SPRING,SUMMER2024 FROM WUFOO WHERE EntryId = {}".format(entryid)
    cursor.execute(query)
    entity_list = cursor.fetchone()
    return entity_list


def populatetable(conn):
    """
    Checking the existence of table and return correct number of user entries.
    :param conn: connection to the database
    :return: list of user entries
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='WUFOO';")
    entity_list = cursor.fetchall()
    if len(entity_list) == 0:
        create_wufootable(conn)
        uri = base_url + 'forms' + formhashkey + 'entries.json'
        print(uri)
        return getentries(uri)
    elif len(entity_list) == 1:
        entryid = str(cursor.execute("SELECT coalesce(max(EntryId),0) FROM 'WUFOO';").fetchall()[0][0])
        uri = base_url + 'forms' + formhashkey + 'entries.json?Filter1=EntryId+Is_greater_than+' + entryid
        print(uri)
        return getentries(uri)


def main():
    conn: Connection = create_database("wufuform.db")

    entries = populatetable(conn)
    # print(json.dumps(entries, indent=4, sort_keys=True))
    for i in entries:
        insert_data(conn, i)
    # Show all records from DB may not require in a production setting
    showalldbentries(conn)
    conn.close()
    # save the entries to entities.json
    with open("entities.json", "a") as outfile:
        json.dump(entries, outfile, indent=4)
    uvicorn.run(app, host="0.0.0.0", port=8000)


app = FastAPI()


@app.get("/forms")
def hello():
    conn = create_database("wufuform.db")
    return returnalldbentries(conn)


@app.get("/formsgui")
def hellogui():
    conn = create_database("wufuform.db")
    return returnguientries(conn)


@app.get("/formsgui/{entryid}")
def entry(entryid=1):
    conn = create_database("wufuform.db")
    return getentry(conn, entryid)


if __name__ == "__main__":
    main()
