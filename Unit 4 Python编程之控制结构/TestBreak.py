# TestBreak.py
sum=0
number=0
while number<20:
    number += 1    # a=a+1 => a+=1
    sum += number
    if sum>100:
        break
print("The number is ",number)
print("The sum is ",sum)
