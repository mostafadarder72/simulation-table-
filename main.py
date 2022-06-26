from dataclasses import dataclass

liat=[0,5,4,2,3,4,3,1,3,5]
lst=[2,3,7,8,6,5,4,7,2,8]
@dataclass
class Row:
    IAT: int = 0
    St: int = 0
    Arrival: int = 0
    Sstart: int = 0
    Send: int = 0
    waiting: int = 0
    Qlen: int = 0
    spend_time: int =0

size = 10
simtable = []
# first customer
c1 = Row()
Iat = liat[0]
St = lst[0]
c1.IAT = Iat
c1.ST = St
c1.Arrival = Iat
c1.Sstart = Iat
c1.Send = c1.Sstart + St
c1.waiting = 0
c1.Qlen = 0
simtable.append(c1)

# all customers
for i in range(1, size):
    c = Row()
    Iat = liat[i]
    St = lst[i]
    c.IAT = Iat
    c.ST = St
    c.Arrival = simtable[i - 1].Arrival + Iat
    if c.Arrival > simtable[i - 1].Send:
        c.Sstart = c.Arrival
        c.Send = c.Sstart + St
        c.waiting = 0
    else:
        c.Sstart = simtable[i - 1].Send
        c.waiting = simtable[i - 1].Send - c.Arrival
        c.Send = c.Sstart + St
    q_count = 0
    j = i-1
    while (c.Arrival < simtable[j].Sstart):
        q_count += 1
        j -= 1
    c.Qlen = q_count
    c.spend_time=c.Send-c.Arrival
    simtable.append(c)

print('# \t IAT \t ST \t arrival \t sstart \t send \t waiting \t queulenth')
i = 0
for x in simtable:
    print(i, "\t", x.IAT, "\t", x.ST, "\t", x.Arrival, "\t\t", x.Sstart, "\t\t", x.Send, "\t\t", x.waiting,"\t\t",x.Qlen)
    i += 1
