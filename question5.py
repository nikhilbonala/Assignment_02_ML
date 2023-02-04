#question5
string="The quick Brow Fox"
upper=0     #counter to store upper letters
lower=0     #counter to store lower letters
for i in string:        #for loop to iterate through string
    if(i==" "):         #skip if encounter space
        continue
    if(i.isupper()):        #isupper return true if string is in upper case
        upper=upper+1
    else:                   #else case is islower case
        lower=lower+1

print("lower=",lower)
print("upper=",upper)



