import sqlite3
import PySimpleGUI as sg
import requests

# Connect to the database
conn = sqlite3.connect('wufuform.db')
cur = conn.cursor()

# To retrieve entries from FastAPI server
response = requests.get('http://localhost:8000/formsgui/')
entries = response.json()

sg.theme('DarkBlue2')

# Define the GUI layout
left_list_column = [
    [sg.Text('CUBES PROJECT LIST', font=('Helvetica', 20))],
    [sg.Text('SELECT AN ENTRY')],
    [sg.Listbox(values=[], size=(50, 15), key='entry_list')],
    [sg.Button('Show Details'), sg.Button('Exit')],
]

right_list_column = [
    [sg.Text('DETAILED ENTRY RECORD', font=('Helvetica', 20))],
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

# Create the window
window = sg.Window('My Entries', layout, resizable=True)
window.finalize()
window['entry_list'].update(values=entries)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Show Details':
        # Retrieve the selected entry from the local database
        # print(values['entry_list'])
        entryid = values['entry_list'][0][0]
        # print(entryid)
        # Retrieve entries from FastAPI Server
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

# Close the connection to the database
conn.close()

# Close the window
