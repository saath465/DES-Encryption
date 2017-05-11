'''
Python module to convert binary string into message.
The message or each block is divided into 6-bit blocks and the eqivalent integer number is obtained
if the number is between 1-26 --> converted to Character
between 27-36 --> converted to number
37 --> '.'
38 --> ' '
'''

Decode = []

def decode(message):
    i = 0
    while(i < len(message)):
        con = message[i:i+6]
        dec = int(''.join(map(str,con)),2)
        
        if 1<=dec<=26:
            Decode.append(chr(dec+96))

        elif 27<=dec<=36:
            Decode.append(str(dec-27))
            
        elif dec == 37:
            Decode.append('.')
     
        elif dec == 38:
            Decode.append(' ')
         

        i = i + 6
    return (''.join(map(str,Decode)))                   #return the final converted message.
