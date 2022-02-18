#H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς. Χρησιμοποιείστε αρχικά την διεύθυνση 
# https://drand.cloudflare.com/public/latest για να βρείτε ποιος είναι ο τελευταίος γύρος και στην συνέχεια πάρτε τις τελευταίες 100 τιμές 
# (πεδίο randomness) μέσα από το https://drand.cloudflare.com/public/{round}. Μετατρέψτε αυτές τις τιμές σε δυαδικό και εμφανίστε το μήκος
#  της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά και το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενες μονάδες.
from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
print(data)
print(type(data))

b=data.decode()
print(type(b))

x=b[9:16]
print(x)

mylist=[]
l=[]
for i in range (x,x-100,-1):
   r=Request.get( 'https://drand.cloudfrare.com/public/{round}'%(i)), 
   mylist.append(data["randomness"])
   
   def funct(letter):
    number = ord(letter)
    return number
    
   for n in mylist:
        w='{0:b}'.format(funct(n))
        l.append(w)

#ευρεση συνεχομενων max 0 και 1
max1=-1
max2=-1
y=l[0]
for i in range(1,len(l)):
      y+=l[i]
s0=0
s1=0
for i in range(len(y)):
    if y[i]=='0':
       s0+=1
    else:
        if max2<s0:
            max2=s0
        s0=0
    if(i==len(y)) and max2<s0:
        max2=s0
for i in range(len(y)):
   if y[i]=='1':
       s1+=1
       if(i==len(y)) and max1<s1:
            max1=s1
        
   else:
        if max1<s1:
            max1=s1
        s1=0

ak0=""
ak1=""
for i in range(max2):
    ak0=ak0 + max2

for i in range(max1):
    ak1=ak1 + max1

print("max1:",ak1,"max2:",ak0)