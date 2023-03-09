from apscheduler.schedulers.blocking import BlockingScheduler
import wufooform
from secrets import base_url, formhashkey, username, password
import requests
import json

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=0, minute=0)
def every_day_job():
    print('This job is run every day at midnight')
    conn = wufooform.create_database("wufuform.db")
    cursor = conn.cursor()

    maxentryid = str(cursor.execute("SELECT coalesce(max(EntryId),0) FROM 'WUFOO';").fetchall()[0][0])
    uri = base_url + 'forms' + formhashkey + 'entries.json?Filter1=EntryId+Is_greater_than+' + maxentryid
    response = requests.get(uri, auth=(username, password))
    entries = response.json()["Entries"]
    if len(entries) > 0:
        for i in entries:
            wufooform.insert_data(conn, i)

        with open("entities.json", "a") as outfile:
            json.dump(entries, outfile, indent=4)
    conn.close()


sched.start()
