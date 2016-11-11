import math
import random

def BitsToDec(bits):
    b=''
    index=len(bits)
    while index>0:
        b+=bits[index]
    return int(b,2)

def ParityBitCoverage(length,ParityPosition):
    a=list()
    #bits covered?
    for x in range(1,length+1):
        if (x&ParityPosition)>0:
            a.append(x)
        x+=1    
    return a

def CheckIsPow2(i):
    return i==pow(2,int(math.log(i,2)))
    
def InsertParityBits(bits):
    #bits is a list
    index=1
    while index<=len(bits):
        if CheckIsPow2(index):
            bits.insert(index-1,0)
        index+=1
    return bits
    
def RemoveParityBits(bits):
    ret=list()
    for x in range(1,len(bits)+1):
        if not(CheckIsPow2(x)):
            ret.append(bits[x-1])
    return ret
        
def Encode(bits,party):
    bits=InsertParityBits(bits)
    index=len(bits)
    while index>0:
        if CheckIsPow2(index):
            coverage=ParityBitCoverage(len(bits),index)
            sumBits=0
            for x in coverage:
                sumBits+=bits[x-1]
            bits[index-1]=CalcParityBit(sumBits,party)
        index-=1
    print 'Message: ',bits,' encoded.'
    return bits

def CalcParityBit(sumBits,party):
    if party=='odd':
        return sumBits%2
    else:
        return (sumBits+1)%2

def VerifyParityBit(bit_value,sumBits,sending_party):
    sumBits
        

def CheckAndCorrectMessage(bits,sending_party):
    error_bit=0
    for x in range(1,len(bits)+1):
        if CheckIsPow2(x):
            if not CheckParityBit(bits,x,sending_party):
                error_bit+=x
    if error_bit!=0:
        print 'Message: ',bits,' correcting bit: ',error_bit
        bits[error_bit-1]=(bits[error_bit-1]+1)%2
        print 'Corrected message: ', bits
    return bits
    
def Decode(bits,party):
    if party=='odd':
        sending_party='even'
    else:
        sending_party='odd'
    bits=CheckAndCorrectMessage(bits,sending_party)
    

def CheckParityBit(bits,bit,sending_party):
    coverage=ParityBitCoverage(len(bits),bit)
    sumBits=0
    for x in coverage:
        sumBits+=int(bits[x-1])
    return CalcParityBit((sumBits+bits[bit-1])%2,sending_party)==bits[bit-1]

def Noise(bits):
    x=random.randint(0,7)
    if x!=0:
        print 'Noise corrupted bit ',x
        bits[x-1]=(bits[x-1]+1)%2
    return bits
    
def StringToList(a):
    x=list()
    for c in a:
        if c in ['1','0']:
            x.append(int(c))
    return x