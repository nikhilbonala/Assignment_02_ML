#question1
n=5
#divided pattern in to 2 parts , first 5 lines and next 4 lines
#1st part
for i in range(0,n):                #for loop(i) to iterate through lines
    for j in range(0,i+1):          #for loop(j) to print stars in the line
        print("*",end="")
    print()
#2nd part
for i in range(0,n-1):              #for loop(i) to iterate through lines
    for j in range(n-1,i,-1):       #for loop(j) to print stars in the line
        print("*",end="")
    print()