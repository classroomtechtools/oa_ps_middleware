"""
Python


"""

DBUSERNAME = ''
HOST = 'localhost'

import requests

APIKEY = '119fa52af433c6304a44f18e866150e9'
payload = {
    'auth_token': APIKEY,
    'since_id': 0
}
url = 'https://igbis.openapply.com/api/v1/students'
app_url = 'powerschool.com'
properties = None

links = []

while True:

    response = requests.get(url, params=payload)
    data = response.json()

    for student in data['students']:
        if properties is None:
            properties = sorted(student.keys())
        print(student.get('id'))
        #print("\n{id}: {name}".format(id=student.get('id'), name=(student.get('first_name') + ' ' + student.get('last_name'))).upper())
        # for prop in properties:
        #   print(' ' * 6, prop, ':', student[prop])
    
    payload['since_id'] = data['students'][-1]['id']            
