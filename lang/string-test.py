input = 123

strinput = str(input)

print(strinput)
#length of string 
print(len(strinput))

strinput = '10'
print(strinput[:len(strinput)-1])#exclude last value

strinput = '100'
print(strinput.rstrip('0'))