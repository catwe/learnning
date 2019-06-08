import os

def search(text, path='.'):
    dir = os.listdir(path)
    for d in dir:
        current = os.path.join(path, d)
        if os.path.isdir(current):
            search(text, current)
        elif d.find(text) > -1:
            print(current)

if __name__ == 'main':
    text = input('input a text: ')
    search(text)