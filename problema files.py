with open('input.txt','r') as f:
    a=f.readline()
nra=0
nrb=0
nrc=0
nro=0
for i in a:
    if ord(i) in range(65,91):
        nra+=1
with open('litereA.txt','w') as f:
    f.write(str(nra))
for i in a:
    if ord(i) in range(97,123):
        nrb+=1
with open('litereB.txt','w') as f:
    f.write(str(nrb))
for i in a:
    if ord(i) in range(49,58):
        nrc+=1
with open('cifre.txt','w') as f:
    f.write(str(nrc))
for i in a:
    if ord(i) in range(33,42):
        nro+=1
with open('operatori.txt','w') as f:
    f.write(str(nro))

