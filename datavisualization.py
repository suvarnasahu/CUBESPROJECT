import sqlite3
import PySimpleGUI as sg
import requests
import smtplib

# create a connection to the database
conn = sqlite3.connect('wufuform.db')
cursor = conn.cursor()

faculty_table = '''
CREATE TABLE IF NOT EXISTS FACULTY
             (bsu_email TEXT PRIMARY KEY,
             first_name TEXT NOT NULL,
             last_name TEXT NOT NULL,
             title TEXT NOT NULL,
             department TEXT NOT NULL);'''
claim_table = '''
CREATE TABLE IF NOT EXISTS CLAIM_TABLE
             (EntryId INTEGER PRIMARY KEY,
             bsu_email TEXT NOT NULL);'''

table_list = [
    faculty_table,
    claim_table
]
# create a table to store user data
for i in table_list:
    cursor.execute(i)

# conn.commit()

# To retrieve entries from FastAPI server
response = requests.get('http://localhost:8000/formsgui/')
entries = response.json()

sg.theme('DarkBlue2')

# Define the GUI layout
left_list_column = [
    [sg.Button('', image_filename='bsu.png')],
    # [sg.Button('CLAIM PROJECT', font=('Helvetica', 14))],
    [sg.Text('CUBES PROJECT LIST', font=('Helvetica', 20))],
    [sg.Text('SELECT A PROJECT')],
    [sg.Listbox(values=[], size=(50, 15), key='entry_list')],
    [sg.Button('Show Details'), sg.Button('Exit')],
]

claim_button = sg.Button('CLAIM', font=('Helvetica', 12), disabled=True)
right_list_column = [
    [sg.Text('DETAILED ENTRY RECORD', font=('Helvetica', 20))],
    [claim_button],
    [sg.Text('Entry ID:'), sg.Text('', key='entry_id')],
    [sg.Text('Prefix:'), sg.Text('', key='PREFIX')],
    [sg.Text('Title:'), sg.Text('', key='title')],
    [sg.Text('Organization Name:'), sg.Text('', key='organization_name')],
    [sg.Text('Organization Website:'), sg.Text('', key='organization_website')],
    [sg.Text('First Name:'), sg.Text('', key='first_name')],
    [sg.Text('Last Name:'), sg.Text('', key='last_name')],
    [sg.Text('Email:'), sg.Text('', key='email')],
    [sg.Text('Phone Number:'), sg.Text('', key='phone_number')],
    [sg.Text(" Interested Collaborative Opportunities", font=('Helvetica', 15))],
    [sg.Checkbox('Course Project', default=False, disabled=True, key='OPP_1')],
    [sg.Checkbox('Guest Speaker', default=False, disabled=True, key='OPP_2')],
    [sg.Checkbox('Site Visit', default=False, disabled=True, key='OPP_3')],
    [sg.Checkbox('Job Shadow', default=False, disabled=True, key='OPP_4')],
    [sg.Checkbox('Internships', default=False, disabled=True, key='OPP_5')],
    [sg.Checkbox('Networking Event', default=False, disabled=True, key='OPP_6')],
    [sg.Checkbox('Career panel', default=False, disabled=True, key='OPP_7')],
    [sg.Text("Collaboration Time Period", font=('Helvetica', 15))],
    [sg.Checkbox('SUMMER 2023', default=False, disabled=True, key='SUMMER2023')],
    [sg.Checkbox('FALL', default=False, disabled=True, key='FALL')],
    [sg.Checkbox('SPRING', default=False, disabled=True, key='SPRING')],
    [sg.Checkbox('SUMMER 2024', default=False, disabled=True, key='SUMMER2024')]

]
layout = [
    [sg.Column(left_list_column),
     sg.VSeperator(),
     sg.Column(right_list_column), ]
]


def getfaculty(email):
    cursor.execute("SELECT bsu_email,first_name, last_name ,title, department FROM FACULTY WHERE bsu_email = ? ;",
                   (email,))
    faculty_list = cursor.fetchone()
    if faculty_list:
        return faculty_list
    else:
        return None


def facultyentry(conn, email, first_name, last_name, title, department):
    cursor = conn.cursor()
    if email and first_name and last_name and title and department:
        cursor.execute("INSERT INTO FACULTY (bsu_email, first_name, last_name,title, department)VALUES(?,?,?,?,?);",
                       (email, first_name, last_name, title, department,))
        print("Data inserted successfully")
        sg.popup('Faculty entry created')
    else:
        sg.popup('Fields Missing please enter')
        print("One or more required fields are missing")
    conn.commit()


def claimentryproject(conn, entryid, bsu_email):
    cursor_claim = conn.cursor()
    cursor_claim.execute("Insert into CLAIM_TABLE(EntryID,bsu_email) values(?,?);", (entryid, bsu_email,))
    conn.commit()


def send_email(values):
    sender_email = 'sssuvarna.sahu@gmail.com'
    sender_password = 'rpjjugyqwcsszlkk'
    receiver_email = values['bsu_email']
    email_subject = 'Thankyou for claiming the Cubes Project'
    message = f"Subject: {email_subject}\n\nHi {values['first_name']},\n\nThanks for submitting your " \
              f"information. Here are the details we received:\n\nBSU Email: {values['bsu_email']}\nFi" \
              f"rst Name: {values['first_name']}\nLast Name: {values['last_name']}\nTitle: " \
              f"{values['title']}\nDepartment: {values['department']}\n\nRegards,\nSuvarna Sahu"
    print(message)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message)
    smtp.quit()
    print("Email Sent to {}".format(receiver_email))


def claim(conn, entryid):
    layout = [[sg.Text('BSU Email: '), sg.Input(key='bsu_email')],
              [sg.Button('Check Email')],
              [sg.Text('First Name: '), sg.Input(key='first_name')],
              [sg.Text('Last Name: '), sg.Input(key='last_name')],
              [sg.Text('Title: '), sg.Input(key='title')],
              [sg.Text('Department: '), sg.Input(key='department')],
              [sg.Button('ClaimProject'), sg.Button('Close')]]

    # create the GUI window
    window = sg.Window('Project Claimed Window', layout)

    # loop to handle events
    while True:
        event, values = window.read()

        # if user clicks the Check Email button
        if event == 'Check Email':
            # check if BSU email already exists in the database
            email = values['bsu_email']
            print(email)  # suvarnasahu@student.bridgew.edu
            user = getfaculty(email)
            print(user)

            if user:
                # if user already exists, populate other details
                window['first_name'].update(user[1])
                window['last_name'].update(user[2])
                window['title'].update(user[3])
                window['department'].update(user[4])
            else:  # if user does not exist, add new user to the database
                sg.popup('Email not found \n Please Enter Faculty details')

        if event == "ClaimProject":
            print("Execution Started")
            email = values['bsu_email']
            user = getfaculty(email)
            if user:
                send_email(values)
                # function to upsert into the claim table
                claimentryproject(conn, entryid, values['bsu_email'])

                sg.popup('Project  Claimed!\nAn email has been sent to the user.')
            else:
                sg.popup('Please Enter Faculty details')
                while values['first_name'] and values['department']:
                    facultyentry(conn, values['bsu_email'], values['first_name'], values['last_name'], values['title'],
                                 values['department'])
                    send_email(values)
                    # function upsert into the claim table
                    claimentryproject(conn, entryid, values['bsu_email'])

                    sg.popup('Project  Claimed!\nAn email has been sent to the user.')

        # if user clicks the Cancel button or closes the window
        elif event == sg.WINDOW_CLOSED or event == 'Close':
            conn.close()
            break
    window.close()


# Create the window
window = sg.Window('My Entries', layout, resizable=True)
window.finalize()
window['entry_list'].update(values=entries)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        conn.close()
        break

    if event == 'Show Details':
        entryid = values['entry_list'][0][0]
        response = requests.get('http://localhost:8000/formsgui/{}'.format(entryid))
        details = response.json()

        # Update the GUI with the details
        window['entry_id'].update(details[0])
        window['PREFIX'].update(details[1])
        window['title'].update(details[2])
        window['organization_name'].update(details[3])
        window['organization_website'].update(details[4])
        window['first_name'].update(details[5])
        window['last_name'].update(details[6])
        window['email'].update(details[7])
        window['phone_number'].update(details[8])
        window['OPP_1'].update(details[9])
        window['OPP_2'].update(details[10])
        window['OPP_3'].update(details[11])
        window['OPP_4'].update(details[12])
        window['OPP_5'].update(details[13])
        window['OPP_6'].update(details[14])
        window['OPP_7'].update(details[15])
        window['SUMMER2023'].update(details[16])
        window['FALL'].update(details[17])
        window['SPRING'].update(details[18])
        window['SUMMER2024'].update(details[19])
        claim_button.update(disabled=False)

    if event == "CLAIM":
        entryid = values['entry_list'][0][0]
        if entryid:
            claim(conn, entryid)
        else:
            sg.popup("Select a project from the left tab")

conn.close()
# Close the window
window.close()
