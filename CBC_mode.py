'''
Created on Mar 20, 2017
This is a module for the CBC mode of encryption where the IV is used in the first round/block to XOR with the Plain-text and fed into the encryption algorithm to produce the 
Cipher-text which is used as an IV for the next round/block.

@author: SaathvikPrasad
'''
import SdesEncrypt
Enc_Message_cbc = []
Dec_Message_cbc = []


'''function for encryption using cbc mode of operation'''
def cbc_des_enc(message,para_key,IV):
    ET = []
    CBC = []
    PdT = []
    i = 0
    ctr = 1
    while(i < len(message)):
        P = message[i:i+12]
        if ctr == 1:
            CBC = SdesEncrypt.exorbits(P,IV)
            ek,PdT = SdesEncrypt.desenc(para_key,CBC)
            
            ET = list(''.join(PdT))
            
            i = i+12
            Enc_Message_cbc.append(''.join(map(str,ET)))
            ctr = ctr+1
        else:
            CBC = SdesEncrypt.exorbits(P, ET)
            ek,PdT = SdesEncrypt.desenc(para_key,CBC)
            
            ET =''.join(PdT)
            
            i = i+12
            ctr = ctr+1
            Enc_Message_cbc.append(''.join(map(str,ET)))
        
    emcbc = ''.join(map(str,Enc_Message_cbc))
    return ek,emcbc


'''function for decryption using cbc mode of operation'''
def cbc_des_dec(msg,para_key,IV):
    Msg = list(msg)
    NIV,PT,ET,PdT = [],[],[],[]
    i = 0
    ctr = 1
    while(i < len(Msg)):
        C = Msg[i:i+12]
        if ctr == 1:
            PdT = SdesEncrypt.desdec(para_key,C)
            ET = ''.join(PdT)
            PT= SdesEncrypt.exorbits(ET,IV)
            i = i+12
            Dec_Message_cbc.append(''.join(map(str,PT)))
            ctr = ctr+1
            NIV = C
        else:
            PdT = SdesEncrypt.desdec(para_key,C)
            ET = ''.join(PdT)
            PT = SdesEncrypt.exorbits(ET, NIV)
            i = i+12
            NIV = C
            ctr = ctr+1
            Dec_Message_cbc.append(''.join(map(str,PT)))
            
    dmcbc = ''.join(map(str,Dec_Message_cbc))
    return dmcbc
    