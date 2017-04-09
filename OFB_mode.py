'''
Created on Mar 20, 2017

This is a module for the OFB mode of encryption where the IV is first fed into the encryption algorithm and the output is then XOR'd with the Plain-text to produce the   
Cipher-text and the output from the algorithm is used as an IV for the next round/block.

@author: SaathvikPrasad
'''
import SdesEncrypt

Enc_Message_ofb = []
Dec_Message_ofb = []


'''function for encryption using OFB mode of operation'''
def ofb_enc(msg,para_key,IV):
    ctr = 1
    i = 0
    ET,CT = [],[]
    while(i<len(msg)):
        P = msg[i:i+12]
        if ctr==1:
            ek,Pdt = SdesEncrypt.desenc(para_key, IV)
            ET = ''.join(Pdt)
            CT = SdesEncrypt.exorbits(ET, P)
            i = i+12
            ctr = ctr + 1
            Enc_Message_ofb.append(''.join(map(str,CT)))
        else:
            ek,Pdt = SdesEncrypt.desenc(para_key, ET)
            ET = ''.join(Pdt)
            CT = SdesEncrypt.exorbits(ET, P)
            Enc_Message_ofb.append(''.join(map(str,CT)))
            i = i + 12
            ctr  =  ctr + 1
    
    emofb = ''.join(map(str,Enc_Message_ofb))
    return ek,emofb



'''function for decryption using OFB mode of operation'''
def ofb_dec(msg,para_key,IV):
    Msg = list(msg)
    PT, ET = [],[]
    ctr = 1
    i = 0
    while(i<len(Msg)):
        C = Msg[i:i+12]
        if ctr == 1:
            ek,Pdt = SdesEncrypt.desenc(para_key, IV)
            ET = ''.join(Pdt)
            PT = SdesEncrypt.exorbits(ET,C)
            Dec_Message_ofb.append(''.join(map(str,PT)))
            i = i + 12
            ctr = ctr + 1
        else:
            ek,Pdt = SdesEncrypt.desenc(para_key, ET)
            ET = ''.join(Pdt)
            PT = SdesEncrypt.exorbits(ET,C)
            Dec_Message_ofb.append(''.join(map(str,PT)))
            i = i + 12
            ctr = ctr + 1
    dmofb = ''.join(map(str,Dec_Message_ofb))
    return dmofb
            
            
             
    
    
    