import requests 

url = "http://text-processing.com/api/sentiment/"
user_input = input("Enter text for sentiment analysis: ")
myobj = {'text': user_input}
response = requests.post(url, data = myobj)
print(response.json())


