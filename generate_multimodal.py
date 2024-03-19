import requests
import base64

# load image
with open('sample.jpg', 'rb') as image_file:
    # read its contents
    image_data = image_file.read()
    # turn it into a base64 string
    image_base = base64.b64encode(image_data)
    # encode as utf8
    base64_string = image_base.decode('utf-8')

api_endpoint = 'http://localhost:11434/api/generate'

data = {
    'model': 'llava',
    'stream': False,
    'prompt': 'Describe the image provided.',
    'images': [base64_string]
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['response'])
else:
    print("Failed to get response")