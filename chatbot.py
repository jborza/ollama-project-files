import requests

api_endpoint = 'http://localhost:11434/api/chat'
messages = []

while True:
    # capture user input
    user_input = input("Enter your message: ")
    # update messages
    data = {
        'model': 'llama2',
        'stream': False,
        'messages': []
    }
    # add the user input to the messages
    messages.append({
        'role': 'user',
        'content': user_input
    })
    for message in messages:
        data['messages'].append(message)


    # send the input to the LLM
    response = requests.post(api_endpoint, json=data)
    # update messages with the response

    if response.status_code == 200:
        response_data = response.json()
        # show the response to the user
        print(response_data['message']['content'])
        messages.append({
            'role': 'assistant',
            'content': response_data['message']['content']
        })
    else:
        print("Failed to get response")





