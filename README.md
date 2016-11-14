#Fuctions

*CheckIsPow2*

1. Input Parameters: x
2. Function: Checks whether x is power of 2
3. Note: a number is power of 2 if the x==power(2,int(log2(x))
4. Return: True/False


*InsertParityBits*

1. Input Parameters: bitMsg
2. Function: Insert a zero in positions that are power of 2, hence in 0,1,2,4,8...
3. Return: bitMsg


*RemoveParityBits*

1. Input Parameters: bitMsg
2. Function: Remove Parity Bits
3. Parity Bits are bits in positions that are power 2
4. Return: bitMsg


*ParityBitCoverage*

1. Input Parameters: msgLength, parityBitPosition
2. Function: returns a list of all positions that are covered by the parity bit.
3. A parity bit covers a bit in a message when the bitwise AND between the bit position and the parity bit position is TRUE.
4. Return: list if positions that are covered by the ParityBit


*CalcParityBit*

1. InputParameters: sumBits, Party
2. Function: Party is either odd or even. odd means that when the sum of the bits is odd, the parity bit is 1, otherwise 0. equally, even means that when the sum  of the bits is even, the parity bit will be 1, otherwise 0.
3. Note: work with %2
4. Return: Parity bit value


*Encode*

1. Input Parameters: bitMsg, Party
2. Function: insert parity bits, calculate their value and return the encoded message
3. use InsertParityBits, ParityBitCoverage and CalcParityBit
4. encoded message


*CheckParityBit*

1. Input Parameters: bitMsg, bit, sending_party
2. Function: Checks whether the value of a parity bit of the received message is correct - based on the values of the bits that are covered by the parity bit.
3. Use ParityBitCoverage and CalcParityBit
4. Return: True/False


*CheckAndCorrectMsg*

1. Input Parameters: bitMsg, sending_party
2. Function: corrects up to 1 wrong bit. Wrong bit's position is the sum of positions of Parity Bits that are wrong
3. Note: Use CheckParityBit. Correct == flip (0 for 1, 1 for 0)
4. Return: bitMsg


*Decode*

1. Input Parameters: bitMsg, party
2. Function: correct the messege is necessary and remove parity bits
3. Note: use CheckAndCorrectMsg, RemoveParityBits
4. Return: bitMsg


*Noise*

1. Input Parameters: bitMsg
2. Function: randomly flip one of the bits
3. Return: bitMsg


*StringToList*

1. Input Parameters: string from the csv file
2. covert to list of 0 and 1 (the bitMsg)
3. Return: bitMsg



**Class: CL_PARTY**

*Attribtues*

1. Party
2. SendingParty


*Init*

1. self.Party=Party
2. self.SendingParty='odd' if party == 'even', and 'even' if party == 'odd'


*GenerateMsg*

1. InputParameters: self, msgLength
2. Function: generate a list of 1 and 0 with the length msgLength


*SendMsg*

1. Input Parameters: self, bitMsg
2. Function: write bitMsg to <party>.csv. first column is a sequence number, 2nd is the message


*SendX*

1. Input Parameters: self, x
2. generate x messages, encode and send them
3. Note: use GenerateMsg, Encode and SendMsg


*ReceiveMsg*

1. Input Parameters: self
2. Function: read <sending_party>.csv, retrieve the messages and print them
3. Note: use Decode, StringToList
