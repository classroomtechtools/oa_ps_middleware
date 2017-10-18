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
columns = None

links = []
response = requests.get(url, params=payload)
json = response.json()

while True:
	payload['since_id'] = json['students'][-1]['id']
	for student in json['students']:
		if columns is None:
			columns = sorted(student.keys())
		print("\n{id}: {name}".format(id=student.get('id'), name=(student.get('first_name') + ' ' + student.get('last_name'))).upper())
		for column in columns:
			print(' ' * 6, column, ':', student[column])
