'''
Created on Mar 20, 2017

This is the ECB mode which takes in the block of plain text and produces an encrypted text using key.
working :: PT-->[[enc(key)]]-->ET
@author: Saathvik
'''

import SdesEncrypt

Enc_Message_ecb = []
Dec_Message_ecb = []

'''function for encryption using ecb mode of operation'''
def ecb_des_enc(Message,para_key):
    i = 0
    while(i < len(Message)):
        PT = Message[i:i+12]
        fk,FET = SdesEncrypt.desenc(para_key, PT)
        Enc_Message_ecb.append(''.join(map(str,FET)))
        i = i + 12
        
    emecb = ''.join(map(str,Enc_Message_ecb))
    return fk,emecb

'''function for decryption using ecb mode of operation'''
def ecb_dec_dec(msg,pk):
    Msg = list(msg)
    PT = []
    FET = []
    i = 0
    while(i < len(Msg)):
        PT = Msg[i:i+12]
        FET = SdesEncrypt.desdec(pk,PT)
        Dec_Message_ecb.append(''.join(map(str,FET)))
        i = i + 12
    dmecb = ''.join(map(str,Dec_Message_ecb))
    return dmecb
    