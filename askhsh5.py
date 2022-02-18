#askhsh5
#Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες. Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με 
#μόνο πεζά γράμματα (μετατρέπετε τα κεφαλαία σε πεζά) και τον κενό χαρακτήρα (space). Αρχικά, χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με 
#το κενό. Στις λέξεις που έχετε υπολογίστε τα ακόλουθα στατιστικά: α) ποιες είναι οι δέκα δημοφιλέστερες λέξεις; Αν κάποιες εμφανίζονται το
#ίδιο πλήθος και βγαίνουν παραπάνω από δέκα, κρατείστε όποιες νομίζετε εσείς ή στην τύχη. β) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί δύο πρώτων 
#γραμμάτων που αρχίζουν οι περισσότερες λέξεις; γ) Επαναλάβετε το ίδιο για τρία γράμματα.

#to programma
f = open('text.txt')
user = str(f.read())
user=user.lower()
user=user.split()
print(user)

word=[]
freq=[]
word.append(user[0])
freq.append(1)
j=1
for i in range(1,len(user),1):
    exist=False
    for w in range(j):
        if word[w]==user[i]:
            exist=True
            idx=w
    if (not exist):
        j+=1
        word.append(user[i])
        freq.append(1)
    else:
        freq[idx]+=1
for i in range(len(freq)):
    for j in range(i+1,len(freq)):
        if freq[i] < freq[j]:
            freq[i],freq[j]=freq[j],freq[i]
            word[i],word[j]=word[j],word[i]
print(word)
print(freq)
for i in range(0,10):
    print(word[i])
#erwtima b
newlist=[]
for i in range(0,len(user)-1):
    temp=user[i]
    newlist.append(temp[0:2])

word2=[]
freq2=[]
word2.append(newlist[0])
freq2.append(1)
j=1
for i in range(1,len(newlist),1):
     exist=False
     for w in range(j):
         if word2[w]==newlist[i]:
             exist=True
             idx=w
     if (not exist):
         j+=1
         word2.append(newlist[i])
         freq2.append(1)
     else:
         freq2[idx]+=1
for i in range(len(freq2)):
     for j in range(i+1,len(freq2)):
         if freq2[i] < freq2[j]:
             freq2[i],freq2[j]=freq2[j],freq2[i]
             word2[i],word2[j]=word2[j],word2[i]
print(word2)
print(freq2)
for i in range(0,3):
     print(word2[i])
#erwtima c

newlist2=[]
for i in range(0,len(user)-1):
    temp=user[i]
    newlist2.append(temp[0:3])

word3=[]
freq3=[]
word3.append(newlist2[0])
freq3.append(1)
j=1
for i in range(1,len(newlist2),1):
     exist=False
     for w in range(j):
         if word3[w]==newlist2[i]:
             exist=True
             idx=w
     if (not exist):
         j+=1
         word3.append(newlist2[i])
         freq3.append(1)
     else:
         freq3[idx]+=1
for i in range(len(freq3)):
     for j in range(i+1,len(freq3)):
         if freq3[i] < freq3[j]:
             freq3[i],freq3[j]=freq3[j],freq3[i]
             word3[i],word3[j]=word3[j],word3[i]
print(word3)
print(freq3)
for i in range(0,3):
     print(word3[i])