import sqlite3
import PySimpleGUI as sg

# Define the GUI population method
list_item = 11
# Fetch data from the database based on the selected list item
conn = sqlite3.connect('wufuform.db')
cursor = conn.cursor()
query = "SELECT * FROM WUFOO WHERE EntryId = {}".format(list_item)
cursor.execute(query)
result = cursor.fetchone()
# print(result)
conn.close()

# Define the GUI layout
layout = [
    [sg.Text('Test CUBES Project Entry', font=('Helvetica', 20))],
    [sg.Text('Entry ID:'), sg.Text('', key='EntryID')],
    [sg.Text('Prefix:'), sg.Text('', key='Prefix')],
    [sg.Text('Title:'), sg.Text('', key='Title')],
    [sg.Text('First_Name:'), sg.Text('', key='First_Name')],
    [sg.Text('Last_Name:'), sg.Text('', key='Last_Name')],
    [sg.Checkbox('Course Project', default=False, disabled=True, background_color="black", key='OPP_1')],
    [sg.Checkbox('Guest Speaker', default=False, disabled=True, background_color="black", key='OPP_2')],
    [sg.Checkbox('Site Visit', default=False, disabled=True, background_color="black", key='OPP_3')],
    [sg.Checkbox('Job Shadow', default=False, disabled=True, background_color="black", key='OPP_4')],
    [sg.Checkbox('Internships', default=False, disabled=True, background_color="black", key='OPP_5')],
    [sg.Checkbox('Networking Event', default=False, disabled=True, background_color="black", key='OPP_6')],
    [sg.Checkbox('Career panel', default=False, disabled=True, background_color="black", key='OPP_7')],
]

# Create the window
window = sg.Window('Test Window', layout)
window.finalize()
window.Element('EntryID').update(result[2])
window.Element('Prefix').update(result[15])
window.Element('Title').update(result[3])
window.Element('First_Name').update(result[20])
window.Element('Last_Name').update(result[21])
window['OPP_1'].update(value=result[8], background_color="black")
window['OPP_2'].update(value=result[9], background_color="black")
window['OPP_3'].update(value=result[10], background_color="black")
window['OPP_4'].update(value=result[11], background_color="black")
window['OPP_5'].update(value=result[12], background_color="black")
window['OPP_6'].update(value=result[13], background_color="black")
window['OPP_7'].update(value=result[14], background_color="black")
# Check if the first name field is populated correctly

assert window.Element('First_Name').Get() == 'Giridhar'
#
# # Check if the last name field is populated correctly
assert window.Element('Last_Name').Get() == 'Samantaray'
#
# # Check if the prefix field is populated correctly
assert window.Element('Prefix').Get() == 'Mr.'
#
# # Check if all the checkboxes are  checked
if window.Element('OPP_1').Get():
    if window.Element('OPP_2').Get():
        if window.Element('OPP_3').Get():
            if window.Element('OPP_4').Get():
                if window.Element('OPP_5').Get():
                    if window.Element('OPP_6').Get():
                        if window.Element('OPP_7').Get():
                            pass

# Close the window
# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # Populate the GUI fields with the fetched data

window.Close()
