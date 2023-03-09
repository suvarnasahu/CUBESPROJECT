import requests


def test_get_data_from_server():
    # Send a GET request to the server endpoint
    response = requests.get('http://localhost:8000/forms/')
    # entries = response.json()
    assert response.status_code == 200

    # Check if the response data contains the expected values expected_data = {'EntryId': 1, 'ORGANIZATION_NAME':
    # 'Sahu', 'FIRSTNAME': 'Suvarna', 'LASTNAME': 'Sahu'} expected_data = [1,"Miss.","Suvarna","Sahu",
    # "ssahu@student.bridgew.edu","7816927488"," Course Project","Guest Speaker","","Job Shadow","","","","",
    # " Fall 2023 (September 2023- December 2023)","",""] expected_data = ["2023-02-08 01:10:44","",15,"chewy",
    # "chewchwy","chewy@gmail.com","http://www.chewy.com","9987430551","","","","","Internships","","","Dr.","",
    # " Fall 2023 (September 2023- December 2023)","","","dia","hock","None"] assert response.json() == expected_data


test_get_data_from_server()
