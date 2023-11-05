alphabets={
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def numToBinary(num):
    sub=''
    while num>=1:
        rem=num%2
        sub+=str(rem)
        num=num//2
    final = sub[::-1]
    return(int(final))

def wordToNum(word):
    word=word.upper()
    num=''
    numList=[]
    for letter in word:
        if (letter.isdigit()):
            num+=letter
        else:
            numList.append(alphabets[letter])
    if num!='':
        numList.append(int(num))
    return numList

def binaryEncodeMessage(message):
    instructions=message.split()
    numList=[]
    encoding=[]
    for instr in instructions:
        numList.append(wordToNum(instr)) #list of each word converted to a list of decimals according to its letters. 
    for word in numList:
        temp=[] #temporary list to store binary encoding of each word 
        for letter in word:
            temp.append(numToBinary(letter))
        encoding.append(temp) #final encoding list that contains binary representations of every word in the message
    print(encoding)



sentence='left10 right up'
binaryEncodeMessage(sentence)