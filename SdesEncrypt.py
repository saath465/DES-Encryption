'''
Created on Mar 7, 2017
This is the general reusable program and method for SDES algorithm. The module contains both the SDES Encryption and Decryption part
@author: SaathvikPrasad
The program is built and executed Eclipse Neon PyDev IDE. 
'''

'''aux function for XOR of 2 blocks'''
def exorbits(L1,L2):
    XB = []
    for i in range(0,len(L1)):
        xb = int(L1[i]) ^ int(L2[i])
        XB.append(xb) 
    return XB    
  
'''S-box 1'''
def findsbox1(L):
    sbox1_0 = ['101', '010', '001', '110', '011', '100', '111', '000']
    sbox1_1 = ['001', '100', '110', '010', '000', '111', '101', '011']
    SB1 = []
    ss = L[1:4]
    ss1 = ''.join(map(str, ss))
    if L[0] == 0:
        s = int(ss1, 2)
        SB1 = sbox1_0[s]
    elif L[0] == 1:
        s = int(ss1, 2)
        SB1 = sbox1_1[s] 
    return SB1

'''S-box 2'''
def findsbox2(L):
    sbox2_0 = ['100', '000', '110', '101', '111', '001', '011', '010']
    sbox2_1 = ['101', '011', '000', '111', '110', '010', '001', '100']
    SB2 = []
    ss = L[1:4]
    ss2 = ''.join(map(str, ss))
    if L[0] == 0:
        s = int(ss2, 2)
        SB2 = sbox2_0[s]
    elif L[0] == 1:
        s = int(ss2, 2)
        SB2 = sbox2_1[s] 
    return SB2
    
'''Encryption part of SDES algorithm'''   
def sdesEncrypt(L,R,kl):
    sdesr = 0
   
    while sdesr < 2:
        print("Round Number::", sdesr)
        RoE = []
        #j = 0
        r3 = R[2]
        r4 = R[3]
        j = 0
        ab = len(R)
        while j < ab:                   #expanding R0==>E(Ro)
            if j == 2:
                RoE.insert(j, r4)
                RoE.insert(j+1, r3)
                j = j + 1
            elif j == 3:
                RoE.insert(j+1, r4)
                RoE.insert(j+2, r3)
                j = j + 1
            elif j == 4 or j == 5:
                RoE.insert(j+2, R[j])
                j = j + 1
            else:
                RoE.insert(j, R[j])
                j = j + 1
       
        KC = []
        for k in range(0,8):            #obtaining 1st 8 bits of key
            KC.append(kl[k])    
        FXB = exorbits(RoE,KC)
        FXB1 = FXB[0:4]
        FXB2 = FXB[4:8]
        S1 = findsbox1(FXB1)            #s-box 1 output
        S2 = findsbox2(FXB2)            #s-box 2 output
        RK = []
        for i in range(0, len(S1)):
            RK.append(S1[i])
        for i in range(0, len(S2)):
            RK.append(S2[i])
        r = exorbits(RK, L)
        R1 = ''.join(map(str, r))
        L1 = R                          
        L = L1                          #new L
        R = R1                          #new R
        kl = kl[1:]+kl[:1]              #shifting key for next round left shift
        sdesr = sdesr + 1
        #print("New L:", ''.join(map(str,L)))
        #print("New R:", ''.join(map(str,R)))
    return kl,L,R     


'''Decryption part of the SDES algorithm'''
def sdesDecrypt(L,R,kl):
    sdesr = 0
   
    while sdesr < 2:
        print("Round Number::", sdesr)
        RoE = []
        #j = 0
        r3 = R[2]
        r4 = R[3]
        j = 0
        ab = len(R)
        while j < ab:                   #expanding R0==>E(Ro)
            if j == 2:
                RoE.insert(j, r4)
                RoE.insert(j+1, r3)
                j = j + 1
            elif j == 3:
                RoE.insert(j+1, r4)
                RoE.insert(j+2, r3)
                j = j + 1
            elif j == 4 or j == 5:
                RoE.insert(j+2, R[j])
                j = j + 1
            else:
                RoE.insert(j, R[j])
                j = j + 1
       
        KC = []
        for k in range(0,8):            #obtaining 1st 8 bits of key
            KC.append(kl[k])    
        FXB = exorbits(RoE,KC)
        FXB1 = FXB[0:4]
        FXB2 = FXB[4:8]
        S1 = findsbox1(FXB1)            #s-box 1 output
        S2 = findsbox2(FXB2)            #s-box 2 output
        RK = []
        for i in range(0, len(S1)):
            RK.append(S1[i])
        for i in range(0, len(S2)):
            RK.append(S2[i])
        r = exorbits(RK, L)
        R1 = ''.join(map(str, r))
        L1 = R                          
        L = L1                          #new L
        R = R1                          #new R
        kl = kl[-1:]+kl[:-1]              #shifting key for next round right shift
        sdesr = sdesr + 1
        print("New L:", ''.join(map(str,L)))
        print("New R:", ''.join(map(str,R)))
    return L,R #return L2,R2 at the end of 2 rounds


'''aux function to call the general SDES method
parameter:: key'''
def desenc(para_key,PT):
    ET = []
    init_L = PT[:6]
    init_R = PT[6:]
    Fk, F_l, F_r = sdesEncrypt(init_L, init_R, para_key)
    ET.append(F_r)
    ET.append(F_l)
    return Fk,ET

def desdec(para_key,PT):
    ET = []
    init_L = PT[:6]
    init_R = PT[6:]
    F_l, F_r = sdesDecrypt(init_L, init_R, para_key)
    ET.append(F_r)
    ET.append(F_l)
    return ET


        


    

            
        
        
        


    



