import hamming_defs
import random
import csv

class cl_party(object):
    msg_received=list([0])    
    msg_sent=list([0])
    
    def __init__(self,party):
        self.party=party
        if party=='even':
            self.opposite_party='odd'
        else:
            self.opposite_party='even'
        
    def GenerateMessage(self):
        b=list()
        for x in range(0,4):
            b.append(random.randint(0,1))
        print 'Message: ',b,' generated.'
        return b
        
    def SendMsg(self,msg):
        msg=hamming_defs.Noise(msg)
        try:
            with open('./messages/'+self.party+'.csv','r+') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                row=list()
                row.append(max(self.msg_received)+1)
                self.msg_sent.append(max(self.msg_sent)+1)
                row.append(msg)
                csvwriter.writerow(row)
                csvfile.close()
        except IOError:
            with open('./messages/'+self.party+'.csv','w') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                row=list()
                row.append(max(self.msg_received)+1)
                self.msg_sent.append(max(self.msg_sent)+1)
                row.append(msg)
                csvwriter.writerow(row)
                csvfile.close()
            
        print 'Message ID: ',row[0],' Message: ',row[1],' sent.'
        
    def SendX(self,x):
        print self.party,' sending ',x,' message(s).'
        for i in range(0,x):
            msg=self.GenerateMessage()
            self.SendMsg(hamming_defs.Encode(msg,self.party))
            
    def ReceiveMsg(self):
        with open('./messages/'+self.opposite_party+'.csv','r') as csvfile:
            csvreader=csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if any(row):
                    if int(row[0]) not in self.msg_received:
                        msg=hamming_defs.Decode(hamming_defs.StringToList(row[1]),self.party)
                        print self.party, '; new message received. ID: ',row[0],' Message: ', msg
                        self.msg_received.append(row[0])
            csvfile.close()


odd=cl_party('odd')
odd.SendX(1)

even=cl_party('even')
even.SendX(1)

print 'Messages sent.'

odd.ReceiveMsg()
even.ReceiveMsg()