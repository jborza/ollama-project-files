import requests
import base64
import csv
import os


def read_image_base64_utf8(image_name):
    # load image
    with open(image_name, 'rb') as image_file:
        # read its contents
        image_data = image_file.read()
        # turn it into a base64 string
        image_base = base64.b64encode(image_data)
        # encode as utf8
        base64_string = image_base.decode('utf-8')
        return base64_string


def run_api_call(base64_string):
    api_endpoint = 'http://localhost:11434/api/generate'

    data = {
        'model': 'llava',
        'stream': False,
        'prompt': 'Act as a bird cataloging AI. Output the name of the bird in image and nothing else.',
        'images': [base64_string]
    }

    response = requests.post(api_endpoint, json=data)

    if response.status_code == 200:
        response_data = response.json()
        print(response_data['response'])
        return response_data['response']
    else:
        print("Failed to get response")
        return None

writer = csv.writer(open('birds.csv', 'w'))
writer.writerow(["File name", "Bird name"])

for filename in os.listdir('birds'):
    # save content as csv file
    image_string = read_image_base64_utf8('birds/{filename}')
    bird_name = run_api_call(image_string)
    writer.writerow([filename, bird_name])
