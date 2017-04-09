'''
Created on Mar 16, 2017
'''

'''
This is a program to  the SDES algorithm
the program takes in a combination of characters and numbers and produces an encrypted text of the input in binary.

@author: SaathvikPrasad.
The program is built and executed Eclipse Neon PyDev IDE. 
'''

#import sys
import re
import datetime
import ECB_mode
import CBC_mode
import OFB_mode
import CTR_mode
import random


'''list for holding message and encrypted message'''
MESSAGE = []


'''function to get the key from the user and produce the julian calendar number
Function borrowed from Assignment 3 template'''
def keyin():
    # date in year.month.day eg: 2017.03.02
    date = input("Enter date in year.month.date")
    date_format = '%Y.%m.%d'
    # converting it to date format of python
    date_input = datetime.datetime.strptime(date, date_format)
    # converting it to time tuple
    time_tuple = date_input.timetuple()
    return time_tuple.tm_yday
    # returning the julian date
    #return time_tuple.tm_yday

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


'''Main Program'''
        
if __name__ == "__main__":
    
    print("Welcome to DES encryption")
    print("Message name and ID should be 10 chars each")
    message = input("Your name and ID in the following format 'name[space]ID[fullstop]:::")
    
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
   
    #Get key from user 
    
    keygen = keyin()
    key = format(keygen, "09b")
    kl = list(key)
    
    
    
    #choose the mode of encryption
    mode = input("Enter the mode of encryption you want to use: 1. ECB, 2. CBC, 3. OFB 4. CTR:::")
    
    # ECB MOde
    if mode == '1':
        fk,Enc_messages_ecb = ECB_mode.ecb_des_enc(MESSAGE, kl)
        print("\n\nDecryption part\n\n")
        fk = fk[-1:]+fk[:-1]
        Dec_message_ecb = ECB_mode.ecb_dec_dec(Enc_messages_ecb, fk)
        print("Final encrypted output using ECB mode for the input string:", message, "is")
        print(Enc_messages_ecb)
        print("Message before encryption is: ") 
        print(''.join(map(str,MESSAGE)))
        print("Message after decryption is: ")
        print(Dec_message_ecb)
        
    # CBC Mode
    elif mode == '2':
        iv = input("Enter your initials as IV::")
        init_iv = encode_map_string(iv)
        IV = list(init_iv)
        fk,Enc_message_cbc = CBC_mode.cbc_des_enc(MESSAGE,kl,IV)
        print("Final encrypted output using CBC mode for the input string:", message, "is")
        print(Enc_message_cbc)
        fk = fk[-1:]+fk[:-1]
        print("\n\nDecryption of Message\n\n")
        Dec_message_cbc = CBC_mode.cbc_des_dec(Enc_message_cbc, fk, IV)
        print("Message before encryption is:")
        print(''.join(map(str,MESSAGE)))
        print("Message after decryption is: ")
        print(Dec_message_cbc)
        
    # OFB Mode    
    elif mode == '3':
        iv = input("Enter your initials as IV::")
        init_iv = encode_map_string(iv)
        IV = list(init_iv)
        Enc_message_ofb = OFB_mode.ofb_enc(MESSAGE, kl, IV)
        print("\n\nDecryption part\n\n")
        Dec_message_ofb = OFB_mode.ofb_dec(Enc_message_ofb, kl, IV)
       
        print("Message before encryption is:")
        print(''.join(map(str,MESSAGE)))
        print("Message after decryption is: ")
        print(Dec_message_ofb)
        
    # CTR Mode    
    elif mode == '4':
        nonce = len(MESSAGE)
        counter = nonce + random.randint(0,99)
        
        fk , Enc_msg_ctr = CTR_mode.ctr_enc(MESSAGE, kl, counter)
       
        #print(counter)
        print("\n\nDecryption part\n\n")
        Dec_msg_ctr = CTR_mode.ctr_dec(Enc_msg_ctr,kl, counter)
        
        print("Encrypted message is::")
        print(Enc_msg_ctr)
        print("Message before encryption is:")
        print(''.join(map(str,MESSAGE)))
        print("Message after decryption is: ")
        print(Dec_msg_ctr)
        
        
    
    
    
    
    


