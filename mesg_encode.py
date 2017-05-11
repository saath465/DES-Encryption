'''
Python module to handle the conversion of string data into binary (6 digits) format.
'''
import re

MESSAGE = []

''' to encode string to decimal to binary
Function borrowed from Assignment 3 template
parameter::string of characters'''
def encode_map_string(input_string):
    # get the length of the input string
    length = len(input_string)
    binary = ""
    # looping through the length of string
    for i in range(0, length):
        # ord is to get the ASCII value of input string negate it the value of a and add 1 to it
        # format is to get the output in 6 bit format for your block
        binary += format((ord(input_string[i]) - ord('a') + 1), '06b')
        #print(binary)
    return binary

'''to encode numbers to decimal to binary
Function borrowed from Assignment 3 template
parameter::string of numbers'''
def encode_map_numbers(input_numbers):
    # get the length of input numbers
    length = len(input_numbers)
    binary = ""
    for i in range(0, length):
        binary += format((ord(input_numbers[i]) - ord('0') + 27), '06b')
    return binary

'''to encode space to binary
parameter::space'''
def encode_map_space(spc):
    if spc == ' ':
        deci_sp = 38
        bin_sp = format(deci_sp, "06b")
    return bin_sp

'''to encode dot to binary
parameter::dot'''
def encode_map_dt(dt1):
    if dt1 == ".":
        deci_dt = 37
        bin_dt = format(deci_dt, "06b")
    return bin_dt

'''aux function for initial message
parameter::message'''
def app_message(mssg):
    for i in range(0, len(mssg)):
        MESSAGE.append(mssg[i])

#function to split the messages in text, numbers, space and dot and convert them to binary and create a message sequence.
def encode_to_bin(message):
    
    msgrx = re.compile(r'(\d+|\s)')
    msg = msgrx.split(message)
    messplit = [x for x in msg if x != '']
    msgalpha = encode_map_string(messplit[0])
    messp = encode_map_space(messplit[1])
    messnum = encode_map_numbers(messplit[2])
    messdt = encode_map_dt(messplit[3])
    msa = list(str(msgalpha))
    app_message(msa)
    mss = list(str(messp))
    app_message(mss)
    msn = list(str(messnum))
    app_message(msn)
    msd = list(str(messdt))
    app_message(msd)
    return ''.join(map(str,MESSAGE))


