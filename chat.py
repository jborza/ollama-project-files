import requests

api_endpoint = 'http://localhost:11434/api/chat'

data = {
    'model': 'llama2',
    'stream': False,
    'messages': [
        {
            'role': 'user',
            'content': 'Hello, I would like to order a pizza.'
        },
        # {
        #     'role': 'assistant',
        #     'content': 'Sure! What type of pizza would you like to order?'
        # },
        # {
        #     'role': 'user',
        #     'content': 'I would like a pepperoni pizza.'
        # }
    ]
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['message'])
else:
    print("Failed to get response")