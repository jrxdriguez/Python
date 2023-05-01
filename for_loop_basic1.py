#1 basic
for i in range(0,151):
    print(i)


#2 multiples of five
for i in range(5,1005,5):
    print(i)


#3 counting the dojo way
for i in range(1,101):
    print(i)
    if i % 10==0:
        print("Coding Dojo")
    elif i % 5==0:
         print("Coding ")
      

#4 whoa
def sumoddnum():
    numbers = range(0,500001)
    total=0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total        
print (sumoddnum())


#5 coutdown by fours
for i in range(2018,0,-4):
    print(i)


# flexible counter
lowNum = 7
highNum = 49
mult = 5

for i in range(lowNum, highNum):
    if i % mult == 0:
       print(i)

