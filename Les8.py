fil = open('File123.txt', "w")
while True:
    s = input()
    if s == '':
        break
    fil.write(s+'\n')
fil.close()
