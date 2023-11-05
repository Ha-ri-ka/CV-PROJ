encoding={
    'left':[1100, 101, 110, 10100],
    'right':[10010, 1001, 111, 1000, 10100],
    'forward': [110, 1111, 10010, 10111, 1, 10010, 100],
    'backward': [10, 1, 11, 1011, 10111, 1, 10010, 100],
    'up': [10101, 10000],
    'down': [100, 1111, 10111, 1110]
}

code={
    'left': 1100,
    'right': 10010,
    'forward': 110,
    'backward': 10,
    'up': 10101,
    'down': 100
}

revCode={
    1100: 'left ',
    10010: 'right ',
    110: 'forward ',
    10: 'backward ',
    10101: 'up ',
    100: 'down '
}

def decodeBinaryToMessage(binary):
    message=''
    for part in binary:
        message+=revCode[part[0]]
    print(message)

binary=[[1100, 101, 110, 10100], [10010, 1001, 111, 1000, 10100], [10101, 10000]]
decodeBinaryToMessage(binary)