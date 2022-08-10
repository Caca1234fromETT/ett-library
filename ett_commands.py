import requests
import json

def get(name):
    c = requests.get('https://tikolu.net/edit/.text/' + name).text
    return c

def post(name, content):
    values = {
        'content': content,
        'timestamp': None,
        'ignoreconflict': True,
    }
    c = requests.post('https://tikolu.net/edit/' + name, json = values)
    return c

while True:
    cmd = input()
    if cmd == "p":
        arg = input()
        index = arg.find(" ")
        name = arg[0 : index]
        content = arg[index + 1 : len(arg)]
        post(name, content)
    elif cmd == "g":
        arg = input()
        print(get(arg))
    else:
        print("error: not a command")
