import sys

tokens = []

with open(sys.argv[1],'r') as file:
    for line in file.readlines():
        tmp = line.split()
        tokens.append(tmp[0] + ' ' + tmp[1])

with open(sys.argv[1],'w') as file:
    for i, token in enumerate(tokens):
        if(i == len(tokens) - 1):
            file.write(token)
        else:
            file.write(token + '\n')