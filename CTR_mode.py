'''
Created on Mar 21, 2017

This is a module for the CTR mode of encryption where the Counter is used as an IV and is first fed into the encryption algorithm and the output is then XOR'd with the Plain-text to produce the   
Cipher-text and the counter is incremented at every block of encryption round and the same process is followed.

@author: SaathvikPrasad
'''
import SdesEncrypt


Enc_Message_ctr = []
Dec_Message_ctr = []


'''aux function to encode the counter to binary 12 chars'''
def encode_counter(ctr):
    ct = format(ctr, "012b")
    C = list(ct)
    return C


    
'''function for encryption using CTR mode of operation'''
def ctr_enc(message,para_key,ctr):
    i = 0
    CT = []
    C = []
    P = []
    while(i<len(message)):
        P = message[i:i+12]
        C = encode_counter(ctr)
        ek, ctrT = SdesEncrypt.desenc(para_key, C)
        CpT = ''.join(ctrT)
        CT = SdesEncrypt.exorbits(CpT, P)
        Enc_Message_ctr.append(''.join(map(str,CT)))
        i = i + 12
        ctr = ctr + 1
        
    emctr = ''.join(map(str,Enc_Message_ctr))
    return ek, emctr


'''function for decryption using CTR mode of operation'''
def ctr_dec(message,pk,ctr):
    C = []
    P = []
    CT = []
    Msg = list(message)
    i = 0
    while(i<len(Msg)):
        C = Msg[i:i+12]
        P = encode_counter(ctr)
        ek,ctrT = SdesEncrypt.desenc(pk,P)
        Cpt = ''.join(ctrT)
        CT = SdesEncrypt.exorbits(Cpt,C)
        Dec_Message_ctr.append(''.join(map(str,CT)))
        i = i+12
        ctr = ctr+1
        
    dmctr = ''.join(map(str,Dec_Message_ctr))
    return dmctr

    