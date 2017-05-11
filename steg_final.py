'''

This is a program to hide a text information in the .png image file.
The program was written,built and executed in Linux Mint platform and with python 2.7 version...

The program has functions such as:
col2hexa--> this is used to convert the r,g,b value to their hexadecimal equivalent.
hex2col--> this is used to convert the hexadecimal value back to the r,g,b value.
encode--> this is used to encode the binary message into the image's hexa value.
decode--> this is used to decode the hexadecimal value into its binary value and remove the message from the image file.
hide_message--> this is used to hide each digit of the binary in the image by calling the 'encode' function.
retrieve_message--> this is used to retrieve the binary format of the message by calling the 'decode' function.

The method used here is to encode each binary value in the LSB of the blue range of colours.
Hence N here is taken as 24, i.e R,G,B each 8 bits..

The method first looks at the Hex value of the blue range's LSB and if the value is between or within the range of 0-5,
the method will embed the binary value '0' or '1' in the place.

While decoding the method looks for values '0' & '1' and retrieves them from the place and replces the hex value.


'''

from PIL import Image           #import Image from Python Image Library.
import optparse
import mesg_encode
import dec

#utility function to convert r,g,b value to the hexadecimal value.
def col2hexa(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)


#utility function to convert hexadecimal value to the r,g,b value.
def hex2col(hexa):
    return tuple(map(ord, hexa[1:].decode('hex')))


#function to encode a binary bit value in the pixel's Least Significant Bit(LSB)
def encode(hexa, digit):
    if hexa[-1] in ('0','1','2','3','4','5'):       #check if the hexadecimal values fall in the range of 0-5 for the blue range of the colour
        hexa = hexa[:-1]+digit          #embed the digit(single binary value) in the place.
        return hexa
    else:
        return None                     #if not skip that pixel.

#function to decode and retrieve a binary bit value in the pixel's Least Significant Bit(LSB)
def decode(hexa):
    if hexa[-1] in ('0','1'):
        return hexa[-1]
    else:
        return None

#function to encode the binary stream in the image file
def hide_message(filename,message):
    img = Image.open(filename)
    binary = mesg_encode.encode_to_bin(message) + '1111111111111110'                #convert the message to binary and add a delimitter.
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        data = img.getdata()

        newVal = []
        digit = 0                                                                   #utility variable for binary stream.
        temp = ''
        for it in data:
            if (digit < len(binary)):
                newpix = encode(col2hexa(it[0],it[1],it[2]),binary[digit])              #encoding the binary to image
                if newpix == None:
                    newVal.append(it)
                else:
                    r,g,b = hex2col(newpix)                                         #encoding the new value to the r,g,b values
                    newVal.append((r,g,b,255))
                    digit +=1
            else:
                newVal.append(it)
        img.putdata(newVal)
        img.save(filename, "PNG")                                                   #save the new file as image
        return "complete"

    return "Incomplete...error"


#function to decode the binary stream in the image file
def retrieve_message(filename):
    img = Image.open(filename)
    binary = ''

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        data = img.getdata()

        for it in data:
            digit = decode(col2hexa(it[0],it[1],it[2]))                         #retrieving the binary digits from the image hex files
            if digit == None:
                pass
            else:
                binary = binary + digit
                if (binary[-16:] == '1111111111111110'):                        #checking for delimitter
                    print("Successful")
                    return dec.decode(binary[:-16])
        return dec.decode(binary)
    return "Error...!"

#parser function to handle the input and options of encoding or decoding.
def Main():
    parser = optparse.OptionParser('usage %prog '+\                             
                                   '-e/-d <target file>')
    parser.add_option('-e' , dest = 'hide', type='string',\
                      help = 'target picture path to hide')
    parser.add_option('-d', dest='retrieve', type='string',\
                      help='target file to retrieve the text')
    (options,args) = parser.parse_args()
    if (options.hide != None):
        text = raw_input("Enter a message to hide:")
        print(hide_message(options.hide,text))
    elif (options.retrieve != None):
        print(retrieve_message(options.retrieve))
    else:
        print(parser.usage)
        exit(0)

if __name__ == '__main__':
    Main()
    
