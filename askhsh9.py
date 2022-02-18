#Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό μήκους 7.
#  Υπολογίστε ποια είναι η μεγαλύτερη ακολουθία από συνεχόμενα 0 και από συνεχόμενα 1.

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
        mylist.append(x)
    print(mylist)
    return mylist

f = open('text.txt')
txt = str(f.read())
encodeThis = txt
l=loopThrough(encodeThis)
max1=-1
max2=-1
x=l[0]
for i in range(1,len(l)):
      x+=l[i]
print(x)
s0=0
s1=0
for i in range(len(x)):
    if x[i]=='0':
        s0+=1
    else:
        if max2<s0:
            max2=s0
        s0=0
    if(i==len(x)) and max2<s0:
        max2=s0
for i in range(len(x)):
    if x[i]=='1':
        s1+=1
        if(i==len(x)) and max1<s1:
            max1=s1
        
    else:
        if max1<s1:
            max1=s1
        s1=0

print("max1:",max1,"max2:",max2)