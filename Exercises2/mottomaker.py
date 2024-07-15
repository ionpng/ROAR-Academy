import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "motto.txt")

def print_content():
    with open(path, 'r') as file:
        content = file.read()
        print(content)

with open(path, 'w') as file:
    file.write("Fiat Lux!")

print_content()

with open(path, 'a') as file:
    file.write('\nLet there be light!')

print_content()
