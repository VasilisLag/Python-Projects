import re

def arithmetic_arranger(numlist,flag):
    firnum = list()
    secnum = list()
    nums = list()
    eq = list()
    #Getting the individual numbers and the operation
    for i in numlist:
        nums = re.findall('[0-9]+',i)
        pra = re.findall('[+,-]',i)
        eq.append(pra[0])
        firnum.append(nums[0])
        secnum.append(nums[1])

    #Printing the first line , the first numbers of all the operations
    for k in firnum:
        if int(k) < 10:
            print("      ", k,end="")
        elif int(k)<100:
            print("     ", k, end="")
        elif int(k)<1000:
            print("    ", k, end="")
        else:
            print("   ", k, end="")
    print('')
    count = 0
    #Printing the second line , the second numbers of all the operations
    for l in secnum:
        if int(l) < 10:
            print("    ",eq[count], l,end="")
        elif int(l)<100:
            print("   ",eq[count], l, end="")
        elif int(l)<1000:
            print("  ",eq[count], l, end="")
        else:
            print(" ",eq[count], l, end="")
        count = count + 1
    print('')

    #Printing the necessary number of underscores
    for z in range(len(firnum)):
        numflag = max(int(firnum[z]),int(secnum[z]))
        if numflag < 10 :
            print("     ___",end="")
        elif numflag < 100 :
            print("    ____",end="")
        elif numflag < 1000 :
            print("   _____",end="")
        else:
            print("  ______",end="")

    print('')

    #Printing the result of the operations
    for z in range(len(firnum)):
        if eq[z] == '+':
            res = int(firnum[z]) + int(secnum[z])
        else:
            res = int(firnum[z]) - int(secnum[z])
        if res > 0:
            if abs(res) < 10:
                print("      ",res,end="")
            elif abs(res) < 100 :
                print("     ",res,end="")
            elif abs(res) < 1000 :
                print("    ",res,end="")
            elif abs(res) <10000:
                print("   ",res,end="")
            else:
                print("  ", res, end="")
        else:
            if abs(res) < 10:
                print("     ",res,end="")
            elif abs(res) < 100 :
                print("    ",res,end="")
            elif abs(res) < 1000 :
                print("   ",res,end="")
            elif abs(res) < 10000:
                print("  ",res,end="")
            else :
                print(" ",res,end="")

#~Start of the MAIN programm~
numlist = list()
while True :
    praksh = input('Give praksh : ')
    if praksh == 'done':
        break
    #Checking if there are alphabetical characters in the input
    if re.findall('[a-z,A-Z]+', praksh):
        print("Characters found , only digits allowed")
        break
    #Checking if the operation ,that the user gave as input, is not either addition or substraction
    if re.findall('[*,/]',praksh):
        print("Multiplication and Division not supported !!!")
        break
    #Checking if any of the numbers has more than 4 digits and if more than 2 numbers were given as input
    nums = re.findall('[0-9]+',praksh)
    if int(nums[0])>9999 or int(nums[1])>9999 :
        print('You inserted number out of range !!!')
    if len(nums)>2:
        print('You inserted more numbers than you should!!!')

    numlist.append(praksh)
#Checking if more than 5 operations were given
if len(numlist)<=5:
    arithmetic_arranger(numlist, False)
else :
    print("Error : too many problems!!!")
print("")