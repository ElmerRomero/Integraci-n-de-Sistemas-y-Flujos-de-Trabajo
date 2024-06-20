import requests
import csv
import time

while True:
    response = requests.get('http://127.0.0.1:5000/data')
    data = response.json()
    with open('data.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Column1', 'Column2'])
        for row in data:
            writer.writerow(row)
    time.sleep(60)
