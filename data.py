
from random import choice


colors = ("yellow", "blue", "green", "red", "orange", "purple")


def new_secret_code():
    new_secret = []
    for i in range(4):
        while True:
            color = choice(colors)
            if color in new_secret:
                continue
            new_secret.append(color)
            break
    
    return f'{new_secret[0]} {new_secret[1]} {new_secret[2]} {new_secret[3]}'

print(list( new_secret_code().split()))