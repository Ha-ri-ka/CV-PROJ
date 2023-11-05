encoding={
    'left':[1100, 101, 110, 10100],
    'right':[10010, 1001, 111, 1000, 10100],
    'forward': [110, 1111, 10010, 10111, 1, 10010, 100],
    'backward': [10, 1, 11, 1011, 10111, 1, 10010, 100],
    'up': [10101, 10000],
    'down': [100, 1111, 10111, 1110]
}

def encodeMessage(message):
    instructions=message.split()
    # numList=[]
    encodedMsg=[]
    for instr in instructions:
        if instr=='left':
            encodedMsg.append(encoding['left'])
        elif instr=='right':
            encodedMsg.append(encoding['right'])
        elif instr=='forward':
            encodedMsg.append(encoding['forward'])
        elif instr=='backward':
            encodedMsg.append(encoding['backward'])
        elif instr=='up':
            encodedMsg.append(encoding['up'])
        elif instr=='down':
            encodedMsg.append(encoding['down'])
        


message='left right up down'
encodeMessage(message)