import sqlite3
import requests
import secrets


def test_countcheck():
    """
    method retrieves data from web and check the right number of data entries
    :return:
    """
    uri = 'https://ssahu.wufoo.com/api/v3/forms/mxys8nv044etu7/entries.json'

    response = requests.get(uri, auth=(secrets.username, secrets.password))
    print(response)
    entries = response.json()
    print(response.json())

    # Create an urllib3 PoolManager with basic authentication
    # http = urllib3.PoolManager(
    #     headers=urllib3.util.make_headers(basic_auth=f"{secrets.username}:{secrets.password}")
    # )
    #
    # response = http.request('GET', uri)
    # entries = json.loads(response.data.decode('utf-8'))
    print(entries["Entries"])
    print('Number of records from WUFOO API: ', len(entries["Entries"]))
    print(len(entries["Entries"]))

    conn = sqlite3.connect("wufuform.db")
    cursor = conn.cursor()
    cursor.execute("Select * from WUFOO;")
    entity_list = cursor.fetchall()
    print('Number of records retrieved through db: ', len(entity_list))
    conn.close()
    assert len(entity_list) == len(entries['Entries'])


test_countcheck()
