#num = 1537268433268
#1) count of digits
count = 0
num = int(input("Enter The Number : "))
print(num)

while (num > 0) :
    count = count +1
    num = num//10
print("The numberof digit are in given numberis : ", count)
