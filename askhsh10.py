#Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό μήκους 7. 
# Από αυτούς κρατάτε μόνο τα πρώτα δύο και τα τελευταία δύο bits. Χωρίστε την ακολουθία σας σε αριθμούς των 16 bits
#  και εμφανίστε τα ακόλουθα στατιστικά: α) Τι ποσοστό είναι ζυγοί; β) Τι ποσοστό διαιρείται ακριβώς με το 3; 
# γ) Τι ποσοστό διαιρείται ακριβώς με το 5; δ) Τι ποσοστό διαιρείται ακριβώς με το 7;

def toAscii(letter):
    number = ord(letter)
    return number

def loopThrough(message):
    mylist=[]
    for n in message:
        print(n)
        print(toAscii(n))
        print('{0:b}'.format(toAscii(n)))
        x='{0:b}'.format(toAscii(n))
        y=x[:2]
        i=x[5:7]
        mylist.append(y+i)
    
            
    print(mylist)
    return mylist

f = open('text.txt')
txt = str(f.read())
encodeThis = txt
l=loopThrough(encodeThis)
x=l[0]
for i in range(1,len(l)):
      x+=l[i]
print(x)

l2=[]
for i in range(0,len(x),17):
    l2.append(x[i:i+16])

while len(l2[len(l2)-1])<16:
    w='0'+l2[len(l2)-1]
    l2[len(l2)-1] = w

w= []
d= []
for i in l2:
    w= list(i)
    j=0
    d1=0
    for z in x:
        z= int(z)
        d1+=(2^1)* z
        j+=1
    d.append(d1)
print(d)


pl2=0
pl3=0
pl5=0
pl7=0
for i in range(len(d)):
    if((d[i] % 2)==0):
        pl2+=1
    if((d[i] % 3)==0):
        pl3+=1
    if((d[i] % 5)==0):
        pl5+=1
    if((d[i] % 7)==0):
        pl7+=1
if pl2!=0:
    P2=((len(d)/pl2)*100)
    print('to pososto twn arithmwn poy einai zugoi einai iso me:',P2)
else:
    print('den yparxoun zugoi arithmoi')

if pl3!=0:
    P3=((len(d)/pl3)*100)
    print('to pososto twn arithmwn poy diaireitai akribws me to 3 einai iso me:',P3)
else:
    print('den yparxoun arithmoi pou diairountai me to 3')

if pl5!=0:
    P5=((len(d)/pl5)*100)
    print('to pososto twn arithmwn poy diaireitai akribws me to 5 einai iso me:',P5)
else:
    print('den yparxoun arithmoi pou diairountai me to 5')

if pl7!=0:
    P7=((len(d)/pl7)*100)
    print('to pososto twn arithmwn poy diaireitai akribws me to 7 einai iso me',P7)
else:
    print('den yparxoun arithmoi pou diairountai me to 7')