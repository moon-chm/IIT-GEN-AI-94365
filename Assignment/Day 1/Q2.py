number=(input("Enter a number: "))
#print number direct
print("Number :",number)
#count even and odd digits
even=0
odd=0
for digit in number:
    if digit.isdigit():
        if int(digit)%2==0:
            even+=1
        else:
            odd+=1
print("Number of even digits: ",even)
print("Number of odd digits: ",odd)
